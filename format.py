# Time : 2022/12/12 10:02
import json
import os

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
def ResumeSDK_Result_format():

    path = 'ResumeSDK_Result'
    tar_path = 'ResumeSDK_Result_format'
    files = os.listdir(path)
    for file in files:
        f = open(os.path.join(path,file), 'r', encoding='utf-8')
        dataStr = f.read()
        data = json.loads(dataStr)

        dict = {}
        dict['name'] = data['result']['name']

        print(dict)
        ff = open(os.path.join(tar_path,file), 'w', encoding='utf-8')
        ff.write(json.dumps(dict, indent=4, ensure_ascii=False))


def hitlant_format():
    path = 'hitalent_result'
    tar_path = 'hitalent_result_format'



if __name__ == '__main__':
    ResumeSDK_Result_format()