#!/usr/bin/python3
"""make use of command line arguments"""

if __name__ == "__main__":
    import requests
    from sys import argv

    arg = {"email": argv[2]}
    res = requests.post(argv[1], data=arg)
    print(res.text)