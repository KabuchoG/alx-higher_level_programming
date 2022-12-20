#!/usr/bin/python3
"""Fetches a web resource"""

from urllib import request

res = request.Request('https://alx-intranet.hbtn.io/status')
with request.urlopen(res) as response:
    result = response.read()
print(result)
