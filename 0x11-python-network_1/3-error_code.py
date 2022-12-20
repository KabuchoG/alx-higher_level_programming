#!/usr/bin/python3
"""Handle eXCEPTIONS"""

if __name__ == "__main__":
    from urllib import parse, request, error
    from sys import argv

    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
