#!/usr/bin/python3
"""make use of command line arguments"""

if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
        