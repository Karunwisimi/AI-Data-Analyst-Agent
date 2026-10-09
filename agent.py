import ollama
from tools import get_customer_count, get_top_categories, get_channel_count

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_customer_count",
            "description": "Returns the number of unique customers in the retail dataset.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_top_categories",
            "description": "Returns the top product categories in the retail dataset.",
            "parameters": {
                "type": "object",
                "properties": {
                    "n": {
                        "type": "integer",
                        "description": "The number of top product categories to return."
                    }
                },
                "required": []
            }
        }
    },
    
    {
        "type": "function",
        "function": {
            "name": "get_channel_count",
            "description": "Returns the number of records for a specified sales channel, such as ONLINE or OFFLINE.",
            "parameters": {
                "type": "object",
                "properties": {
                    "channel": {
                        "type": "string",
                        "description": "The sales channel to count: ONLINE or OFFLINE."
                    }
                },
                "required": ["channel"]
            }
        }
    }
]

user_question = input("What would you like to know about the dataset? ")

messages = [
    {
        "role": "user",
        "content": user_question
    }
]

response = ollama.chat(
    model="qwen2.5:3b",
    messages=messages,
    tools=tools
)

if response.message.tool_calls:
    tool_call = response.message.tool_calls[0]
    tool_name = tool_call.function.name
    arguments = tool_call.function.arguments

    print("Tool requested:", tool_name)
    print("Arguments:", arguments)

    if tool_name == "get_customer_count":
        result = get_customer_count()
        print(f"The dataset contains {result:,} unique customers across all files.")

    elif tool_name == "get_top_categories":
        n = arguments.get("n", 10)
        result = get_top_categories(n)

        print("Top product categories:")
        for category, count in result.items():
            print(f"{category}: {count:,} records")

    elif tool_name == "get_channel_count":
        channel = arguments.get("channel", "").upper()

        if channel not in ["ONLINE", "OFFLINE"]:
            print("Sorry, I can only count ONLINE or OFFLINE records.")
        else:
            result = get_channel_count(channel)
            print(f"There are {result:,} {channel.lower()} records.")

    else:
        print("Sorry, the requested tool is not supported.")

else:
    print(response.message.content)