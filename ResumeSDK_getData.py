# Time : 2022/12/12 14:17
import os

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
'''
    ResumeSDK 通过接口上传简历的base64编码, 可以直接拿到json格式的结果
    AppCode: 54efffd08f1d4f79aaeeb4bdc3e6d7b2
'''

import base64
import requests
import json
import safeRun

def test_parse(file_):
    # 读取文件内容
    cont = open(file_, 'rb').read()
    # base_cont = base64.b64encode(cont)  # python2
    base_cont = base64.b64encode(cont).decode('utf8')  # python3

    # 构造json请求
    data = {
        'file_name': file_,  # 简历文件名（需包含正确的后缀名）
        'file_cont': base_cont,  # 简历内容（base64编码的简历内容）
        'need_avatar': 0,  # 是否需要提取头像图片
        #'ocr_type': 1,  # 1为高级ocr
    }

    url = 'http://resumesdk.market.alicloudapi.com/ResumeParser'

    appcode = '54efffd08f1d4f79aaeeb4bdc3e6d7b2'
    headers = {'Authorization': 'APPCODE ' + appcode,
               'Content-Type': 'application/json; charset=UTF-8',
               }
    # 发送请求
    data_js = json.dumps(data)
    res = safeRun.run('post',url=url, json=data, headers=headers, proxies=proxies)

    # 解析结果
    res_js = json.loads(res.text)
    print(json.dumps(res_js, indent=4, ensure_ascii=False))  # 打印全部结果

    return res_js


if __name__ == '__main__':
    file_dir = r'C:\Users\Administrator\Desktop\简历解析量化测试'
    tar_dir = r'Step1_origdata/ResumeSDK_Result'
    files = os.listdir(file_dir)
    exjsons = os.listdir('Step1_origdata\ResumeSDK_Result')
    for file in files :
        if f'{file}.json' not in exjsons:
            file_ = os.path.join(file_dir,file) # 拼接完整路径
            try:
                parser_result = test_parse(file_)
                f = open(f'{tar_dir}\{file}.json', 'w', encoding='utf-8')
                f.write(json.dumps(parser_result, indent=4, ensure_ascii=False))
                f.flush()
                f.close()
            except Exception as e:
                print(f"{file} : {e}")