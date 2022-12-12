# Time : 2022/12/9 16:11
import json


import requests
proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

def run(method, url, headers,json = None, proxies = proxies, showInfo = 'false'):

    while True:
        try:
            resp = getattr(requests,method)(url, headers = headers, proxies = proxies, json = json)
            break
        except Exception as e:
            print(e)

    if showInfo == 'true':
        print(json.dumps(resp.json()))
        #print(json.dumps(resp.json(), indent=4, ensure_ascii=False))
    elif showInfo == 'false':
        pass

    return resp

if __name__ == '__main__':
    header = {'authorization': 'Bearer 7dbf24ec-6204-4e60-bd5b-0766b3898c45'}
    url = 'https://api.hitalentech.com/api/v1/login'
    payload = {"username": "cindy", "password": "Cindy@123456"}


    resp = run('post',url,header,payload,showInfo='true')
