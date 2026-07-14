import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

print("=== Warehouse Assistant ===")
print("Type 'quit' to exit\n")

# History list — naya add kiya
conversation_history = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    # History mein add karo
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a helpful warehouse assistant for Amazon Fulfillment Center. Help associates with inventory queries, picking routes, safety procedures, and general warehouse operations.",
        messages=conversation_history
    )
    
    # Bot response
    bot_response = message.content[0].text
    
    # Bot ka response bhi history mein add karo
    conversation_history.append({
        "role": "assistant",
        "content": bot_response
    })
    
    print(f"Bot: {bot_response}\n")