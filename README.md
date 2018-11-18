# json-paginator

![PyPI Version](https://img.shields.io/pypi/v/json-paginator.svg)
![License](https://img.shields.io/pypi/l/json-paginator.svg)

A generator for iterating over paginated JSON API responses

## Installation

```
pip install json-paginator
```

## Usage

Instantiate `JsonApiPaginator` with:

* A URL to page 1 of the API output
* A function (or lambda) `get_nextpage(url, body)` which describes how to get the next page. Return `None` to stop iteration.

Example:

```py
from json_paginator import JsonApiPaginator

BASE = 'https://galaxy.ansible.com'

def get_next_page(url, body):
    if body['next_link']:
        return BASE +  body['next_link']
    return None

# instantiate the paginator
pages = JsonApiPaginator(
    BASE + '/api/v1/categories/?page=1',
    get_next_page
)

# iterate over the pages
for url, body in pages:
    print("calling %s" % (url))
    print("found %s results" % (len(body['results'])))
```
