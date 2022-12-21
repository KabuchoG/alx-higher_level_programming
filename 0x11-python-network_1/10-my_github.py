#!/usr/bin/python3
"""
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    user = sys.argv[1]
    passw = sys.argv[2]
    cred = HTTPBasicAuth(user, passw)
    res = requests.get("https://api.github.com/user", auth=cred)
    jr = res.json()
    print(jr.get('id'))
