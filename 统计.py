import json
import os

import requests
proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def getResult(type_,file):
    print(f'处理 {file}中..')
    target_dir = 'aaformat'
    #step2_dir = 'Step2_formatdata\hitalent_format'
    step2_dir = f'Step2_formatdata\{type_}_format'
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
    f = open(fr'Result\{type_}\{file}','w', encoding='utf-8')
    #f = open(fr'Result\hitalent\{file}','w', encoding='utf-8')
    f.write(json.dumps(data,indent=4,ensure_ascii=False))
    #print(json.dumps(data,indent=4))

    # f = open('hitalentResult.csv','a', encoding='utf-8')
    # f.write(f'{file},{data["all"]},{data["important"]},{data["desc"]},{data["correct_important"]},,,,,{data["correct_important"]/data["important"]},,,,,{data["correct_desc"]},,,,,{data["additional"]}\n')

if __name__ == '__main__':
    d = os.popen(r'ssh -i C:\Users\Administrator\Desktop\amos1 -p 6000 -L 5000:127.0.0.1:5000 amos@wuhan.hitalent.com')

    # files = os.listdir('aaformat')
    # for file in files:
    #     try:
    #         getResult('Gulu',file)
    #     except Exception as e:
    #         print(f'------------------------ {file} error!!!')

    # hitalent resumeSDK xiaoxi affinda Gulu
    getResult('Gulu','Chris Huang 20211012.doc.json')
