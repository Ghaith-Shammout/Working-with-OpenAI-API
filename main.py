from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def openAIChatRequest(query):
    # Load config from .env
    endpoint = os.getenv("OPENAI_API_ENDPOINT")
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_DEPLOYMENT_MODEL")
    max_tokens = int(os.getenv("OPENAI_MAX_COMPLETION_TOKENS"))
    temperature = float(os.getenv("OPENAI_TEMPERATURE"))

    # Initialize client correctly
    client = OpenAI(base_url=endpoint, api_key=api_key)

    # System message (define assistant behavior)
    system_message = "You are a helpful AI assistant that provides clear and concise answers."

    # Make API request
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": query}
        ],
        max_completion_tokens=max_tokens,
        temperature=temperature
    )

    # Extract response safely
    return response.choices[0].message.content


def main():
    print("AI Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input("What would you like to do?: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = openAIChatRequest(user_input)
        print("\nAssistant:", response, "\n")


if __name__ == "__main__":
    main()