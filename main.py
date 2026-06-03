from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import List, Dict, Optional

# Load environment variables
load_dotenv()




Message = Dict[str, str]


def prompt_builder(system_message: str, shot: Optional[List[Message]], query: str) -> List[Message]:
    """
    Build a chat prompt compatible with OpenAI Chat Completions API.

    Args:
        system_message (str): Instruction or system-level behavior definition.
        shot (List[Message] | None): Few-shot examples (list of role/content dicts).
        query (str): User input question.

    Returns:
        List[Message]: Fully constructed messages list.
    """
    if not system_message or not isinstance(system_message, str):
        raise ValueError("system_message must be a non-empty string")

    if not query or not isinstance(query, str):
        raise ValueError("query must be a non-empty string")

    messages: List[Message] = [{
        "role": "system",
        "content": system_message.strip()
    }]

    # Add system message first

    # Add few-shot examples if provided
    if shot:
        for msg in shot:
            if not isinstance(msg, dict):
                raise ValueError("Each shot item must be a dict with 'role' and 'content'")
            if "role" not in msg or "content" not in msg:
                raise ValueError("Each shot dict must contain 'role' and 'content'")

            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

    # Add final user query
    messages.append({
        "role": "user",
        "content": query.strip()
    })

    return messages



def get_response(query : str) -> str:
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

    # Assistant Message (shot prompting)
    shot = [{"role": "user", "content": "Example Question"},
            {"role": "assistant", "content": "Example Answer"}]

    prompt = prompt_builder(system_message, shot, query)

    # Make API request
    response = client.chat.completions.create(
        model=model,
        messages=prompt,
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

        response = get_response(user_input)
        print("\nAssistant:", response, "\n")


if __name__ == "__main__":
    main()