import ollama

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": """
You are an AI data analyst.

We are working with a retail transaction dataset.

The dataset has these columns:
- PERSON_PUBLIC_KEY
- DATE
- CHANNEL
- PRODUCT_CATEGORY

A basket is identified by:
PERSON_PUBLIC_KEY + DATE + CHANNEL.

Answer the user's question based only on the information provided.

User question:
How many customers are in the dataset?
"""
        }
    ]
)

print(response.message.content)