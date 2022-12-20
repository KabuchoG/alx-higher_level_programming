#!/usr/bin/python3
"""displays the X-Request-Id found in the header of the response"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    headers = 'X-Request-Id'
    fetched = request.Request(argv[1])
    with request.urlopen(fetched) as re:
        res = re.read()
    print(dict(res).get(headers))