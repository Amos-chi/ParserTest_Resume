# Time : 2022/12/12 10:02
import json
import os

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}
def ResumeSDK_format():

    path = 'Step1_origdata/ResumeSDK_Result'
    tar_path = 'Step2_formatdata\\ResumeSDK_format'
    files = os.listdir(path)
    for file in files:
        f = open(os.path.join(path,file), 'r', encoding='utf-8')
        dataStr = f.read()
        data = json.loads(dataStr)

        # fullname
        dict = {}
        dict['fullName'] = data['result']['name']

        # contacts format
        contacts = []
        if data['result'].get('email'):
            cont = {}
            cont['contact'] = data['result']['email']
            cont['type'] = 'EMAIL'
            contacts.append(cont)
        if data['result'].get('email'):
            cont = {}
            cont['contact'] = data['result']['phone']
            cont['type'] = 'PHONE'
            contacts.append(cont)
        if data['result'].get('qq'):
            cont = {}
            cont['contact'] = data['result']['qq']
            cont['type'] = 'QQ'
            contacts.append(cont)
        if data['result'].get('weixin'):
            cont = {}
            cont['contact'] = data['result']['weixin']
            cont['type'] = 'WECHAT'
            contacts.append(cont)

        dict['contacts'] = contacts

        #location
        if data['result'].get('city_norm'):
            dict['location'] = data['result']['city']

        # languages
        if data['result'].get('lang_objs'):
            langList = []
            for l in data['result']['lang_objs']:
                langList.append(l['language_name'])
            dict['languages'] = langList

        # educations
        if data['result'].get('education_objs'):
            eduList = []
            for edu in data['result']['education_objs']:
                edudict = {}
                keys = {
                    'startDate' : 'start_date',
                    'endDate' : 'end_date',
                    'collegeName' : 'edu_college',
                    'degreeLevel' : 'edu_degree',
                    'majorName' : 'edu_major'
                }
                for k in keys.keys():
                    if edu.get(keys[k]):
                        edudict[k] = edu[keys[k]]

                eduList.append(edudict)
            dict['educations'] = eduList

        # experiences
        if data['result'].get('job_exp_objs'):
            expList = []
            for exp in data['result']['job_exp_objs']:
                expdict = {}
                keys = {
                    'description': 'job_content',
                    'companyName': 'job_cpy',
                    'title': 'job_position',
                    'startDate': 'start_date'
                }
                for k in keys.keys():
                    if exp.get(keys[k]):
                        expdict[k] = exp[keys[k]]
                if exp.get('end_date'):
                    if exp['end_date'] == '至今':
                        expdict['current'] = True
                    else:
                        expdict['endDate'] = exp['end_date']
                expList.append(expdict)
            dict['experiences'] = expList

        # skills
        if data['result'].get('skills_objs'):
            skills = []
            for s in data['result']['skills_objs']:
                skillsDict = {}
                skillsDict['skillName'] = s['skills_name']
                skills.append(skillsDict)
            dict['skills'] = skills

        print(f'ResumeSDK_Result_format :  {file}')
        ff = open(os.path.join(tar_path,file), 'w', encoding='utf-8')
        ff.write(json.dumps(dict, indent=4, ensure_ascii=False))

def hitlant_format():
    path = 'Step1_origdata/hitalent_Result'
    tar_path = 'Step2_formatdata/hitalent_format'

    files = os.listdir(path)
    for file in files:
        f = open(os.path.join(path,file), 'r', encoding='utf-8')
        jdata = json.load(f)
        # 判断中文名还是英文名, 选择firstName lastName的拼接方式
        for _char in jdata['firstName']:
            if '\u4e00' <= _char <= '\u9fa5':
                jdata['fullName'] = jdata['lastName'] + jdata['firstName']
            else:
                jdata['fullName'] = jdata['firstName'] + ' ' +  + jdata['lastName']

        del jdata['firstName']
        del jdata['lastName']

        for j in jdata['contacts']:
            contactsKeys = ['createdDate', 'lastModifiedDate', 'sort']
            for e in contactsKeys:
                if j.get(e) or j.get(e) == 0:
                    del j[e]

        for j in jdata['educations']:
            eduKeys = ['id']
            for e in eduKeys:
                if j.get(e) or j.get(e) == 0:
                    del j[e]

        for j in jdata['experiences']:
            expKeys = ['id', 'company']
            for e in expKeys:
                if j.get(e) or j.get(e) == 0:
                    del j[e]

        for j in jdata['skills']:
            skillKeys = ['score', 'firstUsed', 'lastUsed', 'usedMonth', 'id']
            for e in skillKeys:
                if j.get(e) or j.get(e) == 0:
                    del j[e]

        otherKeys = ['start_time', 'last_update_time', 'parser_cost_time', 'fileName', 'page', 'size', 'fileType']
        for e in otherKeys:
            if jdata.get(e) or jdata.get(e) == 0:
                del jdata[e]

        #print(json.dumps(jdata, indent=4, ensure_ascii=False))
        print(f'hitlant_format :  {file}')
        ff = open(f'{tar_path}\{file}', 'w', encoding='utf-8')
        ff.write(json.dumps(jdata, indent=4, ensure_ascii=False))

def affinda_format():
    path = 'Step1_origdata/Affinda_Reuslt'
    tar_path = 'Step2_formatdata/Affinda_format'

    files = os.listdir(path)
    for file in files:
        f = open(os.path.join(path,file), 'r', encoding='utf-8')
        data = json.load(f)
        # 判断中文名还是英文名, 选择firstName lastName的拼接方式
        dict = {}

        # fullName
        for _char in data['name']:
            if '\u4e00' <= _char <= '\u9fa5':
                dict['fullName'] = data['name']['last'] + data['name']['first']
            else:
                dict['fullName'] = data['name']['first'] + ' ' + data['name']['last']

        # contacts
        contacts = []
        if data.get('emails'):
            for i in data['emails']:
                con_dic = {}
                con_dic['contact'] = i
                con_dic['type'] = 'EMAIL'
                contacts.append(con_dic)
        if data.get('phoneNumbers'):
            for i in data['phoneNumbers']:
                con_dic = {}
                con_dic['contact'] = i
                con_dic['type'] = 'PHONE'
                contacts.append(con_dic)
        dict['contacts'] = contacts

        # locations
        if data.get('location'):
            dict['currentLocation'] = {
                "location" : data['location']
            }
            dict['preferredLocations'] = {
                "location" : data['location']
            }

        # languages
        if data.get('languages'):
            dict['languages'] = data['languages']

        # educations
        if data.get('education'):
            dict['educations'] = []
            for i in data['education']:
                educations = {}
                if i['dates']['startDate']:
                    educations['startDate'] = i['dates']['startDate']
                if i['dates']['completionDate']:
                    educations['endDate'] = i['dates']['completionDate']
                if i['dates']['isCurrent'] == True:
                    educations['current'] = True
                if i['organization']:
                    educations['collegeName'] = i['organization']
                if i['accreditation']['educationLevel']:
                    educations['degreeLevel'] = i['accreditation']['educationLevel']
                if i['accreditation']['education']:
                    educations['majorName'] = i['accreditation']['education']
                dict['educations'].append(educations)

        # experiences
        if data.get('workExperience'):
            dict['experiences'] = []
            for i in data['workExperience']:
                experiences = {}
                if i['jobDescription']:
                    experiences['description'] = i['jobDescription']
                if i['organization'] :
                    experiences['companyName'] = i['organization']
                if i['jobTitle'] :
                    experiences['title'] = i['jobTitle']
                if i['dates']['startDate'] :
                    experiences['startDate'] = i['dates']['startDate']
                if i['dates']['endDate'] :
                    experiences['endDate'] = i['dates']['endDate']
                if i['dates']['isCurrent'] == True:
                    experiences['current'] = True
                dict['experiences'].append(experiences)

        # skills
        if data.get('skills'):
            dict['skills'] = []
            for i in data['skills']:
                dict['skills'].append({"skillName": i['name']})



        #print(json.dumps(dict, indent=4 , ensure_ascii=False))
        print(f'affinda_format :  {file}')
        ff = open(os.path.join(tar_path, file), 'w', encoding='utf-8')
        ff.write(json.dumps(dict, indent=4, ensure_ascii=False))

def Xiaoxi_format():
    path = 'Step1_origdata/Xiaoxi_Result'
    tar_path = 'Step2_formatdata/Xiaoxi_format'

    files = os.listdir(path)
    for file in files:
        f = open(os.path.join(path, file), 'r', encoding='utf-8')
        data = json.load(f)
        dict = {}

        # fullname
        dict['fullName'] = data['name']

        # contacts
        for i in data['parsing_result']['contact_info'].keys():
            print(i)






















if __name__ == '__main__':
    #hitlant_format()
    #ResumeSDK_format()
    #affinda_format()
    Xiaoxi_format()


