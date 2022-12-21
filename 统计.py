import json
import os

import requests
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def getResult(file):
    print(f'处理 {file}中..')
    target_dir = 'aaformat'
    step2_dir = 'Step2_formatdata\hitalent_format'
    url = 'http://127.0.0.1:5000/parser/v3/resume/assert_resume'


    files = [
        ('target', (file, open(os.path.join(target_dir,file),'rb'), 'application/json')),
        ('parsed', (file, open(os.path.join(step2_dir,file),'rb'), 'application/json'))
    ]
    resp = requests.post(url, files=files)
    data = resp.json()
    list = []
    for k in data['important_keys'].keys():
        if data['important_keys'][k] :
            list.append(k)
    for k in list:
        del data['important_keys'][k]

    #print(json.dumps(data,indent=4))
    f = open(f'Result\hitalent\{file}','w', encoding='utf-8')
    f.write(json.dumps(data,indent=4,ensure_ascii=False))
    #print(json.dumps(data,indent=4))

if __name__ == '__main__':
    files = os.listdir('aaformat')

    for file in files:
        #if file not in ['2018 cv_ting.pdf.json']:
        try:
            getResult(file)
        except Exception as e:
            print(f'------------------------ {file} error!!!')

    #getResult('IPG-IPEVO-Marketing-郑静芷.pdf.json')