#!/usr/bin/python3
"""script for github commit
"""
if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/"
    user = sys.argv[1]
    repo = sys.argv[2]
    commits = url + "repos/{}/{}/commits".format(user, repo)
    resp = requests.get(commits)
    if resp.status_code == requests.codes.ok and len(resp.text) > 0:
        try:
            my_obj = resp.json()
            for i, obj in enumerate(my_obj):
                if i == 10:
                    break
                if type(obj) is dict:
                    name = obj.get('commit').get('author').get('name')
                    print("{}: {}".format(obj.get('sha'), name))
        except ValueError as invalid_json:
            pass
