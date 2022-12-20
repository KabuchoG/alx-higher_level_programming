#!/usr/bin/python3
"""Json"""

if __name__ == "__main__":
    import sys, requests

    let = {}
    let['q'] = ""
    if len(sys.argv) == 2:
        let['q'] = sys.argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data=let)
    try:
        response = res.json
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
