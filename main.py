import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

if api_key == None:
    raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables. Please set it in your .env file.")

def main():
    print("Hello from aiagent!")
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user", 
                "content": "Why is Boot.dev. such a great place to learn backend development? Use one paragraph maximum."
            }
        ],
    )
    print("Prompt tokens: ", response.usage.prompt_tokens)
    print("Response tokens: ", response.usage.completion_tokens)
    print("Response:")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
