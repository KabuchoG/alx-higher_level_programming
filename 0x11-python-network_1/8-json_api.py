#!/usr/bin/python3
"""Json"""

if __name__ == "__main__":
    import sys, requests

    let = ""
    if len(sys.argv) == 2:
        let = sys.argv[1]
        data = {"q": let}
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        response = res.json()
        if response:
             print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
           print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
