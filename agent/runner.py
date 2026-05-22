import json

from agent.llm import LLMClient

from .prompts import FINAL_ANSWER_PROMPT, TOOL_SELECTION_PROMPT
from .tools.brooklyn_library import BrooklynLibraryClient


class Runner:
    def __init__(self):
        self.library = BrooklynLibraryClient()
        self.llm = LLMClient()

    def run(self, query):
        res = None
        if not query:
            raise ValueError("Query is required")

        tool_request = self.llm.chat(
            [
                {"role": "system", "content": TOOL_SELECTION_PROMPT},
                {"role": "user", "content": query},
            ]
        )
        if not tool_request:
            raise ValueError("No json returned")

        tool_request = json.loads(tool_request)

        if tool_request["tool_name"] == "search_library":
            args = tool_request["arguments"]
            query = args["query"]
            locations = args.get("locations")

            book_data = self.library.search(query, locations)

            final_res = self.llm.chat(
                [
                    {"role": "system", "content": FINAL_ANSWER_PROMPT},
                    {
                        "role": "user",
                        "content": "original query:"
                        + query
                        + " | book search results:"
                        + json.dumps(book_data),
                    },
                ]
            )
            return final_res

        return res
