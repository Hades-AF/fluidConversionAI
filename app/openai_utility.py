import os
from dotenv import load_dotenv
from openai import OpenAI


def openai_processing(content):
    load_dotenv()
    prompt = create_openai_message(content)

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    print("Running AI request...")
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-4o",
        )
        print("Completed AI request.")
        print("AI Response:")
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"Failed to process AI request: {e}")


def create_openai_message(content: str) -> str:
    return (
        "Please analyze the following list of drinks and brands. "
        "Find the fluid ounces per package for each item. "
        "Use proper formatting and search the internet for accurate information. "
        "Example: A 6-pack of beer with 12oz bottles = 72oz. "
        f"{content}"
    )
