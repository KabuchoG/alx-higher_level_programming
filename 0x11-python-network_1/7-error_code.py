#!/usr/bin/python3
"""make use of command line arguments"""

if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        res = requests.get(argv[1])
        print(res.text)
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(res.status_code))
