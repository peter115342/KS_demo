import openai

OPENAI_API_KEY = "sk-myv3r1s3cr35AP1k3yanabp989hwb"


def ask_gpt(prompt):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4.1", messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    ask_gpt("Tell me a joke")
