import requests

class JsonApiPaginator:

    def __init__(self, page1, get_next_page):
        self.next_page = page1
        self.get_next_page = get_next_page

    def __iter__(self):
        while self.next_page:
            r = requests.get(self.next_page)
            r.raise_for_status()
            body = r.json()
            this_page = self.next_page
            self.next_page = self.get_next_page(this_page, body)

            yield (this_page, body)

        raise StopIteration()
