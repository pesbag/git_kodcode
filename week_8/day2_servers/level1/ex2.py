from logging import exception

import requests

def safe_get(url):
    res=requests.get(url)
    json_res=res.json()
    status=res.status_code
    if status==200:
        return json_res
    elif status==404:
        return None
    else:
        raise print(f"Error: the status is {status}")
