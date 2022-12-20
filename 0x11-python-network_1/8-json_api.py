#!/usr/bin/python3
"""Json"""

if __name__ == "__main__":
    import sys, requests

    let = {}
    let['q'] = ""
    if sys.argv[1]:
        let['q'] = sys.argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data=let)
    response = res.json
    try:
        if response:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
