#!/usr/bin/python3
"""POST data"""

if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    val = {"email": argv[2]}
    data = parse.urlencode(val)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
    print(body.decode("utf-8"))
