#!/usr/bin/python3
"""Fetches a web resource"""

if __name__ == "__main__":

    from urllib import request

    res = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(res) as response:
        result = response.read()
    print("Body response:")
    print(" - type: {}".format(type(result)))
    print(" - content: {}".format(result))
    print(" - utf8 content: {}".format(result.decode("utf-8")))