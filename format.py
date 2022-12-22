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
        if data['result'].get('name'):
            dict['fullName'] = data['result']['name']

        # contacts format
        contacts = []
        if data['result'].get('email'):
            cont = {}
            cont['contact'] = data['result']['email']
            cont['type'] = 'EMAIL'
            contacts.append(cont)
        if data['result'].get('phone'):
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
                        if edu[keys[k]] == '至今':
                            edudict['current'] = True
                        else:
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
        newdata = {}
        # 判断中文名还是英文名, 选择firstName lastName的拼接方式
        for _char in jdata['firstName']:
            if '\u4e00' <= _char <= '\u9fa5':
                newdata['fullName'] = jdata['lastName'] + jdata['firstName']
            else:
                newdata['fullName'] = jdata['firstName'] + ' ' + jdata['lastName']

        del jdata['firstName']
        del jdata['lastName']

        for j in jdata['contacts']:
            contactsKeys = ['createdDate', 'lastModifiedDate', 'sort', 'details']
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
            if jdata.get(e) or jdata.get(e) == 0 or jdata.get(e) == '':
                del jdata[e]





        for k in jdata.keys():
            # 删除空字符串和空集合
            if jdata[k] != '' and jdata[k] != [] and jdata[k] != {}:
                newdata[k] = jdata[k]


        #print(json.dumps(newdata, indent=4, ensure_ascii=False))
        print(f'hitlant_format :  {file}')
        ff = open(f'{tar_path}\{file}', 'w', encoding='utf-8')
        ff.write(json.dumps(newdata, indent=4, ensure_ascii=False))

def affinda_format():
    path = 'Step1_origdata/Affinda_Reuslt'
    tar_path = 'Step2_formatdata\\Affinda_format'

    files = os.listdir(path)
    for file in files:
        print(f'affinda_format :  {file}')
        f = open(os.path.join(path,file), 'r', encoding='utf-8')
        data = json.load(f)
        # 判断中文名还是英文名, 选择firstName lastName的拼接方式
        dict = {}

        # fullName
        if data.get('name'):
            for _char in data['name']:
                if '\u4e00' <= _char <= '\u9fa5':
                    dict['fullName'] = data['name']['last'] + data['name']['middle']+ data['name']['first']
                else:
                    dict['fullName'] = data['name']['first'] + ' ' + data['name']['middle'] + ' ' + data['name']['last']

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
        if len(contacts) > 0:
            dict['contacts'] = contacts
        else:
            pass


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
                if i.get('dates'):
                    if i['dates']['startDate']:
                        educations['startDate'] = i['dates']['startDate']
                    if i['dates']['completionDate']:
                        educations['endDate'] = i['dates']['completionDate']
                    if i['dates']['isCurrent'] == True:
                        educations['current'] = True
                if i.get('organization'):
                    if i['organization']:
                        educations['collegeName'] = i['organization']
                if i.get('accreditation'):
                    if i['accreditation']['educationLevel']:
                        educations['degreeLevel'] = i['accreditation']['educationLevel']
                    if i['accreditation'].get('education'):
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
                if i.get('dates') :
                    if i['dates']['startDate']:
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


        print(f'{file} done..')
        #print(json.dumps(dict, indent=4 , ensure_ascii=False))
        ff = open(os.path.join(tar_path, file), 'w', encoding='utf-8')
        ff.write(json.dumps(dict, indent=4, ensure_ascii=False))

def Xiaoxi_format():
    path = 'Step1_origdata/Xiaoxi_Result'
    tar_path = 'Step2_formatdata/Xiaoxi_format'

    files = os.listdir(path)
    for file in files:
        print(f'format file: {file}..')
        f = open(os.path.join(path, file), 'r', encoding='utf-8')
        data = json.load(f)
        dict = {}

        # fullname
        if data.get('english_parsing_result'):
            dict['fullName'] = data['english_parsing_result']['basic_info']['name']


            # contacts
            contacts = []
            if not data['english_parsing_result']['contact_info']['phone_number']  == '':
                contacts.append({
                    "contact": data['english_parsing_result']['contact_info']['phone_number'],
                    "type": "PHONE"
                })
            if not data['english_parsing_result']['contact_info']['email']  == '':
                contacts.append({
                    "contact": data['english_parsing_result']['contact_info']['email'],
                    "type": "EMAIL"
                })
            if not data['english_parsing_result']['contact_info']['wechat']  == '':
                contacts.append({
                    "contact": data['english_parsing_result']['contact_info']['wechat'],
                    "type": "WECHAT"
                })
            if not data['english_parsing_result']['contact_info']['QQ']  == '':
                contacts.append({
                    "contact": data['english_parsing_result']['contact_info']['QQ'],
                    "type": "QQ"
                })
            if not data['english_parsing_result']['contact_info']['home_phone_number']  == '':
                contacts.append({
                    "contact": data['english_parsing_result']['contact_info']['home_phone_number'],
                    "type": "PHONE"
                })
            dict['contacts'] = contacts

            # current_location
            if not data['english_parsing_result']['basic_info']['current_location'] == '':
                dict['currentLocation'] = data['english_parsing_result']['basic_info']['current_location']
            # expect_location
            if not data['english_parsing_result']['basic_info']['expect_location'] == '':
                dict['preferredLocations'] = data['english_parsing_result']['basic_info']['expect_location']

            # languages
            if not data['english_parsing_result']['others']['language'] == []:
                dict['languages'] = data['english_parsing_result']['others']['language']

            # educations
            educations = []
            for i in data['english_parsing_result']['education_experience']:
                edudic = {}
                if i['start_time_year'] != '' :
                    if i['start_time_month'] != '' :
                        edudic['startDate'] = f"{i['start_time_year']}-{i['start_time_month']}-01"
                    else:
                        edudic['startDate'] = f"{i['start_time_year']}-01-01"
                if i['still_active'] == 1:
                    edudic['current'] = True
                else:
                    if i['end_time_year'] != '':
                        if i['end_time_month'] != '':
                            edudic['endDate'] = f"{i['end_time_year']}-{i['end_time_month']}-01"
                        else:
                            edudic['endDate'] = f"{i['end_time_year']}-01-01"
                if i['school_name'] != '':
                    edudic['collegeName'] = i['school_name']
                if i['degree'] != '':
                    edudic['degreeLevel'] = i['degree']
                if i['major'] != '':
                    edudic['majorName'] = i['major']
                educations.append(edudic)
            if len(educations) > 0:
                dict['educations'] = educations

            # experiences
            experiences = []
            for i in data['english_parsing_result']['work_experience']:
                expdic = {}
                if i['description'] != '':
                    expdic['description'] = i['description']
                if i['company_name'] != '':
                    expdic['companyName'] = i['company_name']
                if i['job_title'] != '':
                    expdic['title'] = i['job_title']
                if i['start_time_year'] != '' :
                    if i['start_time_month'] != '' :
                        expdic['startDate'] = f"{i['start_time_year']}-{i['start_time_month']}-01"
                    else:
                        expdic['startDate'] = f"{i['start_time_year']}-01-01"
                if i['still_active'] == 1:
                    expdic['current'] = True
                else:
                    if i['end_time_year'] != '':
                        if i['end_time_month'] != '':
                            expdic['endDate'] = f"{i['end_time_year']}-{i['end_time_month']}-01"
                        else:
                            expdic['endDate'] = f"{i['end_time_year']}-01-01"

                experiences.append(expdic)
            if len(experiences) > 0:
                dict['experiences'] = experiences

            # skills
            dict['skills'] = []
            if data['english_parsing_result']['others']['skills'] != '':
                for i in data['english_parsing_result']['others']['skills']:
                    dict['skills'].append({"skillName": f"{i}"})

        elif data.get('parsing_result'):
            dict['fullName'] = data['parsing_result']['basic_info']['name']

            # contacts
            contacts = []
            if not data['parsing_result']['contact_info']['phone_number'] == '':
                contacts.append({
                    "contact": data['parsing_result']['contact_info']['phone_number'],
                    "type": "PHONE"
                })
            if not data['parsing_result']['contact_info']['email'] == '':
                contacts.append({
                    "contact": data['parsing_result']['contact_info']['email'],
                    "type": "EMAIL"
                })
            if not data['parsing_result']['contact_info']['wechat'] == '':
                contacts.append({
                    "contact": data['parsing_result']['contact_info']['wechat'],
                    "type": "WECHAT"
                })
            if not data['parsing_result']['contact_info']['QQ'] == '':
                contacts.append({
                    "contact": data['parsing_result']['contact_info']['QQ'],
                    "type": "QQ"
                })
            if not data['parsing_result']['contact_info']['home_phone_number'] == '':
                contacts.append({
                    "contact": data['parsing_result']['contact_info']['home_phone_number'],
                    "type": "PHONE"
                })
            dict['contacts'] = contacts

            # current_location
            if not data['parsing_result']['basic_info']['current_location'] == '':
                dict['currentLocation'] = data['parsing_result']['basic_info']['current_location']
            # expect_location
            if not data['parsing_result']['basic_info']['expect_location'] == '':
                dict['preferredLocations'] = data['parsing_result']['basic_info']['expect_location']

            # languages
            if not data['parsing_result']['others']['language'] == []:
                dict['languages'] = data['parsing_result']['others']['language']

            # educations
            educations = []
            for i in data['parsing_result']['education_experience']:
                edudic = {}
                if i['start_time_year'] != '':
                    if i['start_time_month'] != '':
                        edudic['startDate'] = f"{i['start_time_year']}-{i['start_time_month']}-01"
                    else:
                        edudic['startDate'] = f"{i['start_time_year']}-01-01"
                if i['still_active'] == 1:
                    edudic['current'] = True
                else:
                    if i['end_time_year'] != '':
                        if i['end_time_month'] != '':
                            edudic['endDate'] = f"{i['end_time_year']}-{i['end_time_month']}-01"
                        else:
                            edudic['endDate'] = f"{i['end_time_year']}-01-01"
                if i['school_name'] != '':
                    edudic['collegeName'] = i['school_name']
                if i['degree'] != '':
                    edudic['degreeLevel'] = i['degree']
                if i['major'] != '':
                    edudic['majorName'] = i['major']
                educations.append(edudic)
            if len(educations) > 0:
                dict['educations'] = educations

            # experiences
            experiences = []
            for i in data['parsing_result']['work_experience']:
                expdic = {}
                if i['description'] != '':
                    expdic['description'] = i['description']
                if i['company_name'] != '':
                    expdic['companyName'] = i['company_name']
                if i['job_title'] != '':
                    expdic['title'] = i['job_title']
                if i['start_time_year'] != '':
                    if i['start_time_month'] != '':
                        expdic['startDate'] = f"{i['start_time_year']}-{i['start_time_month']}-01"
                    else:
                        expdic['startDate'] = f"{i['start_time_year']}-01-01"
                if i['still_active'] == 1:
                    expdic['current'] = True
                else:
                    if i['end_time_year'] != '':
                        if i['end_time_month'] != '':
                            expdic['endDate'] = f"{i['end_time_year']}-{i['end_time_month']}-01"
                        else:
                            expdic['endDate'] = f"{i['end_time_year']}-01-01"

                experiences.append(expdic)
            if len(experiences) > 0:
                dict['experiences'] = experiences

            # skills
            dict['skills'] = []
            if data['parsing_result']['others']['skills'] != '':
                for i in data['parsing_result']['others']['skills']:
                    dict['skills'].append({"skillName": f"{i}"})

        #print(json.dumps(dict, indent=4, ensure_ascii=False))

        ff = open(os.path.join(tar_path, file), 'w', encoding='utf-8')
        ff.write(json.dumps(dict, indent=4, ensure_ascii=False))




if __name__ == '__main__':
    #hitlant_format()
    ResumeSDK_format()
    #affinda_format()
    #Xiaoxi_format()


