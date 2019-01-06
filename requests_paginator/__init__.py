import requests

class RequestsPaginator:

    def __init__(self, page1, get_next_page):
        self.next_page = page1
        self.get_next_page = get_next_page

    def __iter__(self):
        while self.next_page:
            r = requests.get(self.next_page)
            this_page = self.next_page
            yield r
            self.next_page = self.get_next_page(r)

        return
