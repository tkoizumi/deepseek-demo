from .tools.brooklyn_library import BrooklynLibraryClient


class Runner:
    def __init__(self):
        self.library = BrooklynLibraryClient()

    def run(self, query):
        if not query:
            raise ValueError("Query is required")

        res = self.library.search(query)
        return res
