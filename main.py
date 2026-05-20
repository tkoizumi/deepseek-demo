import sys

from dotenv import load_dotenv

from agent.llm import LLMClient


def main():
    load_dotenv()
    llm = LLMClient()

    if len(sys.argv) < 2:
        print("You need to ask the agent to do something!")
        sys.exit(1)

    query = sys.argv[1]
    print(f'User asked "{query}"')

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Keep answers short.",
        },
        {"role": "user", "content": query},
    ]

    res = llm.chat(messages)
    print(res)


if __name__ == "__main__":
    main()
