import json
import os
import re


# files = os.listdir('aaformat')
#
# for i in files:
#     if i not in  ['Vishal K.docx.json', 'Yi-CHUNG SU.pdf.json', '字节跳动-小荷健康-上海区域BD负责人-马晶晶.pdf.json', '10Product Manager-Xiaohang Fan.pdf.json', 'IPG-IPEVO-Marketing-郑静芷.pdf.json', '114.FPX-MICA-金丛佳-用户体验设计师.pdf.json' , '2018 cv_ting.pdf.json']:
#         f = open(f'aaformat\{i}','r', encoding='utf-8')
#         data = json.load(f)
#
#         if data.get('experiences'):
#             for exp in data['experiences']:
#                 if exp.get('description'):
#                     exp['description'] = re.sub(r'\W+', r'\\W*', exp['description'])
#
#                     ff = open(f'aaformat\{i}','w', encoding='utf-8')
#                     ff.write(json.dumps(data, indent=4, ensure_ascii=False))
#
des = '''Work with business stakeholders to translate business requirement into functional requirement.
Set up the Power BI database, design and develop all the custom metrics, reports and dashboards in Power BI to meet functional
requirements for the whole operation department by cooperating with IT team in Spain.
Clarify end user’s inquiry on reports’ features and functionalities, continuously optimize reports along with the developing
operating procedure.
Collect and consolidate data from different portals to prepare monthly and quarterly operational reports for upper management to
track enterprise level KPI.
Conduct analytical projects on massive datasets with tableau to analyze system operational constraints, deficiencies and defects,
collaborate with operation team and tech team to develop solutions.
Monitor and report on accurate transaction generation at the roadside, timely data transmission, data validation of transaction,
track and analyze system performance and operation performance.
Participate in the implementation and testing of Central Systems, track results and records and escalate system performance issues.'''
print(re.sub(r'\W+', r'\\W*', des))