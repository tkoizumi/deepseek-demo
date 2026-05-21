import json
import sys

from dotenv import load_dotenv

from agent.llm import LLMClient
from agent.runner import Runner


def main():
    load_dotenv()
    # llm = LLMClient()
    runner = Runner()

    if len(sys.argv) < 2:
        print("You need to ask the agent to do something!")
        sys.exit(1)

    query = sys.argv[1]
    # print(f'User asked "{query}"')
    res = runner.run(query)
    print(json.dumps(res, indent=2))

    # messages = [
    #     {
    #         "role": "system",
    #         "content": "You are a helpful assistant. Keep answers short.",
    #     },
    #     {"role": "user", "content": query},
    # ]
    #
    # res = llm.chat(messages)
    # print(res)


if __name__ == "__main__":
    main()
