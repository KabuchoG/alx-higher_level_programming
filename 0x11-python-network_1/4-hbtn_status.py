#!/usr/bin/python3
"""Use requests"""

if __name__ == "__main__":
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    res = res.text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
