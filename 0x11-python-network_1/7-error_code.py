#!/usr/bin/python3
"""script for posting
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    resp = requests.get(url)
    if resp.status_code != requests.codes.ok:
        print('Error code: {}'.format(resp.status_code))
    else:
        print(response.text)
