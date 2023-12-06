#!/usr/bin/python3
"""script for posting to web
"""
if __name__ == "__main__":
    import requests
    import sys
    url = "http:///0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {'q': q}
    resp = requests.post(url, data=query)
    if resp.status_code != requests.codes.ok or len(resp.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            my_obj = resp.json()
            if len(my_obj) == 0:
                print('No result')
                sys.exit()
            my_id = my_obj.get('id')
            my_name = my_obj.get('name')
            print("[{}] {}".format(my_id, my_name))
        except ValueError as invalid_json:
            print('Not a valid JSON')