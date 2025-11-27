import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def ask_gpt(prompt):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4.1", messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    ask_gpt("Tell me a joke")
