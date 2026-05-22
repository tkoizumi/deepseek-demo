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
    res = runner.run(query)
    print(res)


if __name__ == "__main__":
    main()
