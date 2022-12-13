import json
import os

'''
    使用：
        将affinda页面上批量解析简历后生成的json文件放入项目
        修改底8行打开的文件名
        然后脚本会将json文件中 所有简历的parser结果 按文件名 生成json文件 到step1中对应的文件夹
'''

tar_dir = r'Step1_origdata\Affinda_Reuslt'

f = open('affinda-parser-wgbdEwKM.json','r', encoding='utf-8')
data = json.load(f)

for json_ in data['resumes']:
    fileName = f"{json_['meta']['fileName']}.json"
    pr = json_['data']

    ff = open(os.path.join(tar_dir,fileName),'w', encoding='utf-8')
    ff.write(json.dumps(pr, indent=4, ensure_ascii=False))


