import requests


class BrooklynLibraryClient:
    def __init__(self):
        self.base_url = "https://discover.bklynlibrary.org/api/search/index.php"
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://discover.bklynlibrary.org/",
        }
        self.locations = {
            "central": "Central Library",
            "park slope": "Park Slope Library",
        }

    def resolve_locations(self, locations):
        res = []
        for location in locations:
            k = location.lower().strip()
            if k not in self.locations:
                raise ValueError("Not a valid location")
            res.append(self.locations[k])

        return res

    def parse_books(self, data):
        res = []
        groups = data["grouped"]["ss_grouping"]["groups"]
        for group in groups:
            docs = group["doclist"]["docs"]
            for doc in docs:
                id = doc["id"]
                title = doc["title"]
                author = doc.get("author")
                obj = {"id": id, "title": title, "author": author}
                res.append(obj)

        return res

    def search(self, query, locations=None):
        params = {"search": query, "catalog": "true"}
        if locations:
            locs = self.resolve_locations(locations)
            params["availableat"] = "||".join(locs)

        res = requests.get(self.base_url, params=params, headers=self.headers)

        if not res.text.strip():
            raise ValueError("Empty response body")

        return self.parse_books(res.json())
