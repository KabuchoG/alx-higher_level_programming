#!/usr/bin/python3
"""displays the X-Request-Id found in the header of the response"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    head = 'X-Request-Id'
    fetched = request.Request(argv[1])
    with request.urlopen(fetched) as re:
        print(dict(re.headers).get(head))
