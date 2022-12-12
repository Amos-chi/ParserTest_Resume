# Time : 2022/12/12 17:43
import json

import requests


import safeRun
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

url = "https://www.xiaoxizn.com/portrait-upload?parse_mode=general"

payload={}
files=[
  ('resume-file',('单栏正常简历-马晶晶.pdf',open(r'C:/Users/Administrator/Desktop/简历解析量化测试/单栏正常简历-马晶晶.pdf','rb'),'application/pdf'))
]
headers = {}

response = requests.post(url, headers=headers, files=files, proxies=proxies)
print(json.dumps(response.json(), indent=4))