#!/usr/bin/python3
"""Json"""

if __name__ == "__main__":
    import sys, requests

    q = ""
    if sys.argv[1]:
        q = sys.argv
    res = requests.post('http://0.0.0.0:5000/search_user', json=q)
    response = res.json
    try:
        if response:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
