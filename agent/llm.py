import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMClient:
    def __init__(self):
        api_key = os.getenv("DEEPSEEK_API_KEY")

        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found")

        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.model = "deepseek-chat"

    def chat(self, messages):
        res = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0,
        )

        return res.choices[0].message.content

    def json_chat(self, messages):
        res = self.chat(messages)

        import json

        if not res:
            raise Exception("No response from LLM client")

        return json.loads(res)
