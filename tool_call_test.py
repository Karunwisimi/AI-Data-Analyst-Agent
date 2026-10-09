import ollama
import pandas as pd
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


df = pd.read_csv("Data/transactions_part_01.csv")

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

    print("Tool requested:", tool_call.function.name)
    print("Arguments:", tool_call.function.arguments)

    
    if tool_call.function.name == "get_customer_count":
        result = get_customer_count(df)
   
    elif tool_call.function.name == "get_top_categories":
        n = tool_call.function.arguments.get("n", 10)
        result = get_top_categories(df, n)

    elif tool_call.function.name == "get_channel_count":
        channel = tool_call.function.arguments.get("channel", "")
        result = get_channel_count(df, channel)

    else:
        result = "Unknown tool requested."

    messages.append(response.message)

    messages.append({
        "role": "tool",
        "content": str(result)
    })

    if tool_call.function.name == "get_top_categories":
        print("Top product categories:")
        for category, count in result.items():
            print(f"{category}: {count:,} records")
    else:
        final_response = ollama.chat(
            model="qwen2.5:3b",
            messages=messages
            )
        print(final_response.message.content)

else:
    print(response.message.content)