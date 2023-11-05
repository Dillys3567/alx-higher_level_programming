#!/usr/bin/python3
"""script for my github
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    url = "https://api.github.com/"
    user = url + "user"
    usern = sys.argv[1]
    passw = sys.argv[2]
    resp = requests.get(user, auth=HTTPBasicAuth(usern, passw))
    if resp.status_code == requests.codes.ok and len(resp.text) > 0:
        try:
            my_obj = resp.json()
            print(my_obj.get('id'))
        except ValueError as inv:
            print('Not a valid JSON')
    else:
        print(None)
