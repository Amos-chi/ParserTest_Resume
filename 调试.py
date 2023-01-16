# Time : 2023/1/12 15:51
import json
import os

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
files = os.listdir('Step1_origdata/Gulu_Result')
for file in files:
    f = open(f'Step1_origdata/Gulu_Result/{file}','r',encoding='utf-8')
    data = json.load(f)
    try:
        if data['result']['data']['extract_result'].get('language_skills'):
            print(f"{file}: {[i['name'] for i in data['result']['data']['extract_result'].get('language_skills')]}")
    except:
        pass
