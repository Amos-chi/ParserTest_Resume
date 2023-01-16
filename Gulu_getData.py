# Time : 2023/1/12 14:36
import json
import os

import requests

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

def get_GuluData(files):
    url = 'https://official-demo-extract.gllue.com/official_demo_extract_all'
    resp = requests.post(url,files=files,proxies=proxies)
    #print(json.dumps(resp.json(),indent=4,ensure_ascii=False))
    return resp

if __name__ == '__main__':

    dir = r'C:\Users\Administrator\Desktop\简历解析量化测试'
    tar_dir = r'Step1_origdata/Gulu_Result'
    exjsons = os.listdir('Step1_origdata\Gulu_Result')
    files = os.listdir(dir)
    for file in files:
        if f'{file}.json' not in exjsons:
            print(f'正在解析: {file}')
            file_ = os.path.join(dir,file)
            files = [('resume_file',(file, open(file_, 'rb'), 'application/pdf'))]
            try:
                resp = get_GuluData(files)
                f = open(f'{tar_dir}\{file}.json', 'w', encoding='utf-8')
                f.write(json.dumps(resp.json(), indent=4, ensure_ascii=False))
            except Exception as e:
                print(f'{file}: {e}')