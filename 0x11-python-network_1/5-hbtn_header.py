#!/usr/bin/python3
"""Get a header element"""

if __name__ == "__main__":
    from sys import argv
    import requests

    res = requests.get(argv[1])
    response = res.headers
    print(response.get('X-Request-Id'))
