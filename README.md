# requests-paginator

![PyPI Version](https://img.shields.io/pypi/v/requests-paginator.svg)
![License](https://img.shields.io/pypi/l/requests-paginator.svg)

A generator for iterating over paginated API responses

## Installation

```
pip install requests-paginator
```

## Usage

Instantiate `RequestsPaginator` with:

* A URL to page 1 of the API output
* A function (or lambda) `get_nextpage(page)` which describes how to get the next page:
    * Return `None` to stop iteration.
    * `page` is an instance of [`requests.models.Response`](http://docs.python-requests.org/en/master/user/quickstart/#response-content)

Examples:

```py
from requests_paginator import RequestsPaginator

BASE = 'https://galaxy.ansible.com'

def get_next_page(page):
    body = page.json()
    if body['next_link']:
        return BASE +  body['next_link']
    return None

# instantiate the paginator
pages = RequestsPaginator(
    BASE + '/api/v1/categories/?page=1',
    get_next_page
)

# iterate over the pages
for page in pages:
    print("calling %s" % (page.url))
    page.raise_for_status()
    print("found %s results" % (len(page.json()['results'])))
```

```py
from requests_paginator import RequestsPaginator

def get_next_page(page):
    links = {}
    if "Link" in page.headers:
        linkHeaders = page.headers["Link"].split(", ")
        for linkHeader in linkHeaders:
            (url, rel) = linkHeader.split("; ")
            url = url[1:-1]
            rel = rel[5:-1]
            if rel == 'next':
                return url
    return None

# instantiate the paginator
pages = RequestsPaginator(
    'https://api.github.com/users/github/repos?page=1',
    get_next_page
)

# iterate over the pages
for page in pages:
    print("calling %s" % (page.url))
    page.raise_for_status()
    print("found %s results" % (len(page.json())))
```
