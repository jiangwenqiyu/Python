import requests
import json
from selenium import webdriver

# url = 'https://www.zhipin.com/web/boss/recommend'
# browser = webdriver.Chrome()
# browser.get(url)
# with open('新建文本文档.txt') as f:
#     cookies = json.loads(f.read())
# for i in cookies:
#     browser.add_cookie({
#         'domain':i['domain'],
#         'httpOnly':i['httpOnly'],
#         'name':i['name'],
#         'path':i['path'],
#         'secure':i['secure'],
#         'session':i['session'],
#         'storeId':i['storeId'],
#         'value':i['value']
#     })
# browser.refresh()

url = 'https://www.zhipin.com/wapi/zpitem/web/boss/search/geeks.json?page=1&keywords=产品经理&tag=&city=101010100&experience=-10,20&salary=-1,-1&age=0,30&schoolLevel=-1&applyStatus=-1&degree=201,201&source=1'
header = {'accept': 'application/json, text/plain, */*',
          'cookie': '__g=-; __l=r=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fboss%2Frecommend&l=%2Fwww.zhipin.com%2Fweb%2Fboss%2Frecommend&g=&s=3&friend_source=0; JSESSIONID=""; _bl_uid=Idk32iChfn5o045pp5nI24pxtj8C; ___gtid=-1955052366; __fid=1cf98cff472f055192d09eb63502fe88; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1607305699,1607388865,1607394982; lastCity=101010100; wt2=6Pbc9s0u2hfS4mts; _bl_uid=F0k5qf7g3gqlmyh7wlty2tRed30g; JSESSIONID=""; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1607413612; __c=1607394982; __a=81815318.1600144826.1607388865.1607394982.197.11.37.59',
          'referer': 'https://www.zhipin.com/vue/index/',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'}
res = requests.get(url, headers = header).text
print(res)

{
    'code': 0,
    'message': 'Success',
    'zpData': {
        'displayTraineeStyle': 0,
        'heightGray': 0,
        'cityCode': 101010100,
        'advantageShow': 0,
        'hasMore': True,
        'displayAboard': True,
        'hasJobCompetitive': False,
        'jobExperience': 105,
        'geekList': [{
            'encryptGeekId': 'a48093632559fbe91Hd60ti9GFs~',
            'isFriend': 0,
            'talkTimeDesc': None,
            'cooperate': 0,
            'blur': 0,
            'mateName': None,
            'shareNote': None,
            'shareMessage': 0,
            'encryptShareId': None,
            'geekCallStatus': 0,
            'suid': None,
            'geekCard': {
                'securityId': 'RQLylycZ37pn4HHLIG65tCXrbPmU8DB71H9z8Nkv-IflEJmUnSe8qfqZBGr_b8TaiOgNTe6q5tE2rE3-M7t2lQ06VlYjmjiTVlCkXxc-qjC1ttrnV15LC_v9sgULgXLuH68PVNn_3tvlLZUciMwf7ZcxCdVlT3JMUcd3MUGCsTZ5yp3FyT30yWGxErt8zGbcu_g9g25H5XFP5svsAZRZHBTTNAJax7Qj2AeNMdaTU45HO-rtbM7wImC81ZwTlbnjLA-uiBp1xGnCzXxFhr_afNSxFAgUuUKkWznTQMKEtmuHvy1qFpN7sRfydGZKy_1bHFZiWA~~',
                'geekId': 33095089,
                'geekName': '董云扬',
                'geekAvatar': 'https: //img.bosszhipin.com/beijin/upload/avatar/20200128/45705a2b530d6e8985c75e94876a28905ff42b5dcc1feb7b6a911bb7bf83d409_s.jpg',
                'geekGender': 1,
                'geekWorkYear': '5年',
                'geekDegree': '本科',
                'freshGraduate': 0,
                'geekDesc': {
                    'content': '艺术设计系首饰设计专业，热爱时尚及搭配，有较强的男装时尚审美和个人的搭配风格，擅长各类风格的服装搭配。同时对服装文化有相当的了解。工作经验：男装搭配师、企划部男女鞋品牌拍摄的搭配及拍摄方案策划。个人在微信上做服装搭配建议与售卖。性格开朗幽默，善于沟通合作，喜欢高效工作脑子挺快的~',
                    'indexList': []
                },
                'expectId': 105697739,
                'expectType': 0,
                'expectPositionType': 0,
                'salary': '6-11K',
                'lowSalary': 6,
                'highSalary': 11,
                'middleContent': {
                    'content': '老美华鞋业服饰·买手',
                    'indexList': []
                },
                'jobId': 114523811,
                'lid': 'eb7c5c46-fb1d-4aa2-9528-2cb090705180.f1: common.3673-GroupB,3650-GroupC.1',
                'actionDateDesc': None,
                'expectPositionCode': 250104,
                'expectPositionName': '买手',
                'expectPositionNameLv2': '',
                'expectLocationCode': 101010100,
                'expectLocationName': '北京',
                'expectSubLocation': 0,
                'expectSubLocationName': None,
                'applyStatus': 2,
                'applyStatusDesc': '在职-考虑机会',
                'activeTime': 1607415042,
                'birthday': '19950201',
                'ageDesc': '25岁',
                'ageLight': {
                    'content': '25岁',
                    'highlight': False
                },
                'geekEdu': {
                    'id': 0,
                    'userId': 0,
                    'school': '天津美术学院',
                    'schoolId': 0,
                    'major': '时尚服饰设计',
                    'degree': 0,
                    'degreeName': '本科',
                    'eduType': 0,
                    'startDate': '20130101',
                    'endDate': '20180101',
                    'eduDescription': None,
                    'addTime': None,
                    'updateTime': None,
                    'timeSlot': None
                },
                'geekEdus': [{
                    'id': 0,
                    'userId': 0,
                    'school': '天津美术学院',
                    'schoolId': 0,
                    'major': '时尚服饰设计',
                    'degree': 0,
                    'degreeName': '本科',
                    'eduType': 0,
                    'startDate': '2013.01',
                    'endDate': '2018.01',
                    'eduDescription': None,
                    'addTime': None,
                    'updateTime': None,
                    'timeSlot': None
                }],
                'geekWorks': [{
                    'id': 85863209,
                    'geekId': 0,
                    'company': '老美华鞋业服饰',
                    'industryCode': 0,
                    'industry': None,
                    'industryCategory': None,
                    'position': 0,
                    'positionCategory': '买手',
                    'blueCollarPosition': False,
                    'positionName': '买手设计师',
                    'positionLv2': 0,
                    'isPublic': 0,
                    'department': None,
                    'responsibility': '1.资料收集整合总结\n2.鞋包设计改良\n3.采购开发买手选品',
                    'startDate': '2020.07',
                    'endDate': '',
                    'customPositionId': 0,
                    'customIndustryId': 0,
                    'workPerformance': '',
                    'workEmphasisList': ['搭配造型',
                                         '鞋包设计',
                                         '鞋包买手'],
                    'certStatus': 0,
                    'workType': 0,
                    'addTime': None,
                    'updateTime': None,
                    'companyHighlight': {
                        'content': '老美华鞋业服饰',
                        'indexList': []
                    },
                    'positionNameHighlight': {
                        'content': '买手',
                        'indexList': []
                    },
                    'workTime': '5个月',
                    'workMonths': 0,
                    'current': True,
                    'stillWork': True,
                    'startYearMonStr': '2020',
                    'endYearMonStr': '至今',
                    'workTypeIntern': False
                },
                    {
                        'id': 59229389,
                        'geekId': 0,
                        'company': '优美国际贸易',
                        'industryCode': 0,
                        'industry': None,
                        'industryCategory': None,
                        'position': 0,
                        'positionCategory': '策划经理',
                        'blueCollarPosition': False,
                        'positionName': '视觉拍摄策划服装搭配',
                        'positionLv2': 0,
                        'isPublic': 0,
                        'department': None,
                        'responsibility': '1.主要负责公司旗下男女鞋品牌的拍摄方案制定。服装搭配、场地和动作细节等等。\n2.运营公司ins账号\n3.鞋款选款买手',
                        'startDate': '2019.01',
                        'endDate': '',
                        'customPositionId': 0,
                        'customIndustryId': 0,
                        'workPerformance': '',
                        'workEmphasisList': ['买手',
                                             '服装搭配',
                                             '拍摄方案'],
                        'certStatus': 0,
                        'workType': 0,
                        'addTime': None,
                        'updateTime': None,
                        'companyHighlight': {
                            'content': '优美国际贸易',
                            'indexList': []
                        },
                        'positionNameHighlight': {
                            'content': '策划经理',
                            'indexList': []
                        },
                        'workTime': '2年',
                        'workMonths': 0,
                        'current': False,
                        'stillWork': True,
                        'startYearMonStr': '2019',
                        'endYearMonStr': '至今',
                        'workTypeIntern': False
                    },
                    {
                        'id': 24762770,
                        'geekId': 0,
                        'company': '垂衣',
                        'industryCode': 0,
                        'industry': None,
                        'industryCategory': None,
                        'position': 0,
                        'positionCategory': '化妆/造型/服装',
                        'blueCollarPosition': False,
                        'positionName': '服装搭配师',
                        'positionLv2': 0,
                        'isPublic': 0,
                        'department': None,
                        'responsibility': '1.为每个客户根据其需求搭配出服装配饰组合盒子。\n2.公众号推文型录拍摄搭配。',
                        'startDate': '2018.08',
                        'endDate': '2019.01',
                        'customPositionId': 0,
                        'customIndustryId': 0,
                        'workPerformance': '',
                        'workEmphasisList': ['男装搭配',
                                             '造型师',
                                             '服装搭配'],
                        'certStatus': 0,
                        'workType': 0,
                        'addTime': None,
                        'updateTime': None,
                        'companyHighlight': {
                            'content': '垂衣',
                            'indexList': []
                        },
                        'positionNameHighlight': {
                            'content': '化妆/造型/服装',
                            'indexList': []
                        },
                        'workTime': '5个月',
                        'workMonths': 0,
                        'current': False,
                        'stillWork': False,
                        'startYearMonStr': '2018',
                        'endYearMonStr': '2019',
                        'workTypeIntern': False
                    }],
                'geekDoneWorks': None,
                'geekSource': 0,
                'matches': ['选品',
                            '搭配风格',
                            '艺术设计系',
                            '首饰设计',
                            '时尚男装'],
                'markWords': [{
                    'content': '选品',
                    'highlight': False
                },
                    {
                        'content': '搭配风格',
                        'highlight': False
                    },
                    {
                        'content': '艺术设计系',
                        'highlight': False
                    },
                    {
                        'content': '首饰设计',
                        'highlight': False
                    },
                    {
                        'content': '时尚男装',
                        'highlight': False
                    }],
                'encryptGeekId': 'a48093632559fbe91Hd60ti9GFs~',
                'encryptJobId': 'f33dffbddcde9bd51nV-3t--GFNR',
                'eliteGeek': 0,
                'viewed': False,
                'completeType': 0
            },
            'geekLastWork': {
                'id': 85863209,
                'geekId': 0,
                'company': '老美华鞋业服饰',
                'industryCode': 0,
                'industry': None,
                'industryCategory': None,
                'position': 0,
                'positionCategory': '买手',
                'blueCollarPosition': False,
                'positionName': '买手设计师',
                'positionLv2': 0,
                'isPublic': 0,
                'department': None,
                'responsibility': '1.资料收集整合总结\n2.鞋包设计改良\n3.采购开发买手选品',
                'startDate': '2020.07',
                'endDate': '',
                'customPositionId': 0,
                'customIndustryId': 0,
                'workPerformance': '',
                'workEmphasisList': ['搭配造型',
                                     '鞋包设计',
                                     '鞋包买手'],
                'certStatus': 0,
                'workType': 0,
                'addTime': None,
                'updateTime': None,
                'companyHighlight': {
                    'content': '老美华鞋业服饰',
                    'indexList': []
                },
                'positionNameHighlight': {
                    'content': '买手',
                    'indexList': []
                },
                'workTime': '5个月',
                'workMonths': 0,
                'current': True,
                'stillWork': True,
                'startYearMonStr': '2020',
                'endYearMonStr': '至今',
                'workTypeIntern': False
            },
            'showEdus': [{
                'id': 0,
                'userId': 0,
                'school': '天津美术学院',
                'schoolId': 0,
                'major': '时尚服饰设计',
                'degree': 0,
                'degreeName': '本科',
                'eduType': 0,
                'startDate': '2013.01',
                'endDate': '2018.01',
                'eduDescription': None,
                'addTime': None,
                'updateTime': None,
                'timeSlot': None
            }],
            'showWorks': [{
                'id': 85863209,
                'geekId': 0,
                'company': '老美华鞋业服饰',
                'industryCode': 0,
                'industry': None,
                'industryCategory': None,
                'position': 0,
                'positionCategory': '买手',
                'blueCollarPosition': False,
                'positionName': '买手设计师',
                'positionLv2': 0,
                'isPublic': 0,
                'department': None,
                'responsibility': '1.资料收集整合总结\n2.鞋包设计改良\n3.采购开发买手选品',
                'startDate': '2020.07',
                'endDate': '',
                'customPositionId': 0,
                'customIndustryId': 0,
                'workPerformance': '',
                'workEmphasisList': ['搭配造型',
                                     '鞋包设计',
                                     '鞋包买手'],
                'certStatus': 0,
                'workType': 0,
                'addTime': None,
                'updateTime': None,
                'companyHighlight': {
                    'content': '老美华鞋业服饰',
                    'indexList': []
                },
                'positionNameHighlight': {
                    'content': '买手',
                    'indexList': []
                },
                'workTime': '5个月',
                'workMonths': 0,
                'current': True,
                'stillWork': True,
                'startYearMonStr': '2020',
                'endYearMonStr': '至今',
                'workTypeIntern': False
            },
                {
                    'id': 59229389,
                    'geekId': 0,
                    'company': '优美国际贸易',
                    'industryCode': 0,
                    'industry': None,
                    'industryCategory': None,
                    'position': 0,
                    'positionCategory': '策划经理',
                    'blueCollarPosition': False,
                    'positionName': '视觉拍摄策划服装搭配',
                    'positionLv2': 0,
                    'isPublic': 0,
                    'department': None,
                    'responsibility': '1.主要负责公司旗下男女鞋品牌的拍摄方案制定。服装搭配、场地和动作细节等等。\n2.运营公司ins账号\n3.鞋款选款买手',
                    'startDate': '2019.01',
                    'endDate': '',
                    'customPositionId': 0,
                    'customIndustryId': 0,
                    'workPerformance': '',
                    'workEmphasisList': ['买手',
                                         '服装搭配',
                                         '拍摄方案'],
                    'certStatus': 0,
                    'workType': 0,
                    'addTime': None,
                    'updateTime': None,
                    'companyHighlight': {
                        'content': '优美国际贸易',
                        'indexList': []
                    },
                    'positionNameHighlight': {
                        'content': '策划经理',
                        'indexList': []
                    },
                    'workTime': '2年',
                    'workMonths': 0,
                    'current': False,
                    'stillWork': True,
                    'startYearMonStr': '2019',
                    'endYearMonStr': '至今',
                    'workTypeIntern': False
                },
                {
                    'id': 24762770,
                    'geekId': 0,
                    'company': '垂衣',
                    'industryCode': 0,
                    'industry': None,
                    'industryCategory': None,
                    'position': 0,
                    'positionCategory': '化妆/造型/服装',
                    'blueCollarPosition': False,
                    'positionName': '服装搭配师',
                    'positionLv2': 0,
                    'isPublic': 0,
                    'department': None,
                    'responsibility': '1.为每个客户根据其需求搭配出服装配饰组合盒子。\n2.公众号推文型录拍摄搭配。',
                    'startDate': '2018.08',
                    'endDate': '2019.01',
                    'customPositionId': 0,
                    'customIndustryId': 0,
                    'workPerformance': '',
                    'workEmphasisList': ['男装搭配',
                                         '造型师',
                                         '服装搭配'],
                    'certStatus': 0,
                    'workType': 0,
                    'addTime': None,
                    'updateTime': None,
                    'companyHighlight': {
                        'content': '垂衣',
                        'indexList': []
                    },
                    'positionNameHighlight': {
                        'content': '化妆/造型/服装',
                        'indexList': []
                    },
                    'workTime': '5个月',
                    'workMonths': 0,
                    'current': False,
                    'stillWork': False,
                    'startYearMonStr': '2018',
                    'endYearMonStr': '2019',
                    'workTypeIntern': False
                }],
            'activeTimeDesc': '刚刚活跃',
            'anonymousGeek': 0,
            'hasAttachmentResume': 0,
            'haveChatted': 0,
            'hasBg': 0,
            'canUseDirectCall': False,
            'feedback': [{
                'code': 100,
                'memo': '学历不符合要求',
                'showType': 0,
                'titleL2': '学历不符合要求的原因是？',
                'feedbackL2List': [{
                    'code': 103,
                    'memo': '非统招（全日制）',
                    'showType': 0
                },
                    {
                        'code': 104,
                        'memo': '非相关专业',
                        'showType': 0
                    },
                    {
                        'code': 105,
                        'memo': '其他原因',
                        'showType': 1
                    }]
            },
                {
                    'code': 200,
                    'memo': '年龄、性别不合适',
                    'showType': 0,
                    'titleL2': '具体不合适原因是？',
                    'feedbackL2List': [{
                        'code': 201,
                        'memo': '年龄偏大',
                        'showType': 0
                    },
                        {
                            'code': 202,
                            'memo': '年龄偏小',
                            'showType': 0
                        },
                        {
                            'code': 203,
                            'memo': '我的岗位只适合男性',
                            'showType': 0
                        },
                        {
                            'code': 204,
                            'memo': '我的岗位只适合女性',
                            'showType': 0
                        }]
                },
                {
                    'code': 300,
                    'memo': '求职岗位、地点、薪资不合适',
                    'showType': 0,
                    'titleL2': '具体不合适原因是？',
                    'feedbackL2List': [{
                        'code': 301,
                        'memo': '求职意向不是买手',
                        'showType': 0
                    },
                        {
                            'code': 302,
                            'memo': '所在地不是北京',
                            'showType': 0
                        },
                        {
                            'code': 303,
                            'memo': '期望薪资偏高',
                            'showType': 0
                        },
                        {
                            'code': 304,
                            'memo': '牛人不活跃',
                            'showType': 0
                        },
                        {
                            'code': 305,
                            'memo': '牛人不是全职',
                            'showType': 0
                        },
                        {
                            'code': 306,
                            'memo': '其他原因',
                            'showType': 1
                        }]
                },
                {
                    'code': 400,
                    'memo': '工作经历不满意',
                    'showType': 0,
                    'titleL2': '工作经历出现了什么问题？',
                    'feedbackL2List': [{
                        'code': 401,
                        'memo': '买手经验不足',
                        'showType': 0
                    },
                        {
                            'code': 402,
                            'memo': '工作年限太短',
                            'showType': 0
                        },
                        {
                            'code': 403,
                            'memo': '没有大公司经历',
                            'showType': 0
                        },
                        {
                            'code': 404,
                            'memo': '行业经验不足',
                            'showType': 0
                        },
                        {
                            'code': 405,
                            'memo': '跳槽频繁',
                            'showType': 0
                        },
                        {
                            'code': 406,
                            'memo': '简历描述太少',
                            'showType': 0
                        },
                        {
                            'code': 407,
                            'memo': '其他原因',
                            'showType': 1
                        }]
                },
                {
                    'code': 500,
                    'memo': '其他原因',
                    'showType': 1,
                    'titleL2': '',
                    'feedbackL2List': []
                },
                {
                    'code': 600,
                    'memo': '沟通过、面试过、重复推荐',
                    'showType': 0,
                    'titleL2': '具体问题是？',
                    'feedbackL2List': [{
                        'code': 601,
                        'memo': '与牛人沟通过',
                        'showType': 0
                    },
                        {
                            'code': 602,
                            'memo': '约牛人面试过',
                            'showType': 0
                        },
                        {
                            'code': 603,
                            'memo': '重复推荐',
                            'showType': 0
                        },
                        {
                            'code': 604,
                            'memo': '其他原因',
                            'showType': 1
                        }]
                }],
            'feedbackTitle': '选择不喜欢的原因，为您优化推荐',
            'searchChatCardCostCount': 0,
            'friendGeek': False,
            'blurGeek': False
        }]
}
}
