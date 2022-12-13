# Time : 2022/12/12 17:43
import json
import os

import requests


import safeRun
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
def getXiaoxiData(files):
    url = "https://www.xiaoxizn.com/portrait-upload?parse_mode=general"
    response = requests.post(url, files=files, proxies=proxies)
    print(json.dumps(response.json(), indent=4))
    return  response

if __name__ == '__main__':
    file_dir = r'C:\Users\Administrator\Desktop\简历解析量化测试'
    tar_dir = r'Step1_origdata/Xiaoxi_Result'
    files = os.listdir(file_dir)
    for file in files:
        file_ = os.path.join(file_dir, file)  # 拼接完整路径
        files = [('resume-file',(file, open(file_, 'rb'), 'application/pdf'))]
        resp = getXiaoxiData(files)
        f = open(f'{tar_dir}\{file}.json', 'w', encoding='utf-8')
        f.write(json.dumps(resp.json(), indent=4, ensure_ascii=False))