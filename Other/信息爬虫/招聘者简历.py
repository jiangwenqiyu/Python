import requests
import json


def getTotalCount(page):
    print('第{}页'.format(page))
    jobid = 'f33dffbddcde9bd51nV-3t--GFNR'
    url = 'https://www.zhipin.com/wapi/zpboss/h5/boss/recommendGeekList?jobid={}&status=0&source=0&age=16,-1&gender=-1&switchJobFrequency=-1&exchangeResumeWithColleague=0&recentNotView=-1&activation=-1&school=-1&major=0&experience=0&degree=0&salary=0&intention=-1&jobId={}&page={}'.format(jobid, jobid, page)
    # url = 'https://www.zhipin.com/wapi/zpboss/h5/geek/detail/get?expectId=105697739&jid=114523811&lid=abc9505a-96b5-4a99-9c98-3cba41989128.f1:common.3673-GroupB,3650-GroupC.1&wayType=0&sourceType=3&securityId=TckNDoZ7-gXxaLqgP_Ev7zCDi3pjS5vyob13i6Mjz61onkM15Nih9onn_q_qscc3ueYxbpvg6_kSQURCQP0g4J5AigweJuFJ0IZQVxktU_XWMxOaMYzL6J3t0jrY0lI7Yv8fe4Ckq1w8KweGZr_PK4xg1sNKRE6i1dRkXkpRik0_rFWDHLETD-o5i--cKx1xS4j1qoZHnQbQKyKPd4ft37VjvvBIpLSAl0zxblisD7BdJ-CyRgPNyt4eoA69ViX6GyB91NmseHvJthL79h59Ez3zJ8NdVbFzMJKWn53nUSwfizlqBuSrQushmt5f919Pdfun_g~~'
    header = {'accept': 'application/json, text/plain, */*',
              'cookie': '__g=-; __l=r=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fboss%2Frecommend&l=%2Fwww.zhipin.com%2Fweb%2Fboss%2Frecommend&g=&s=3&friend_source=0; JSESSIONID=""; _bl_uid=Idk32iChfn5o045pp5nI24pxtj8C; ___gtid=-1955052366; __fid=1cf98cff472f055192d09eb63502fe88; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1607305699,1607388865,1607394982; lastCity=101010100; wt2=6Pbc9s0u2hfS4mts; _bl_uid=F0k5qf7g3gqlmyh7wlty2tRed30g; JSESSIONID=""; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1607413612; __c=1607394982; __a=81815318.1600144826.1607388865.1607394982.197.11.37.59',
              'referer': 'https://www.zhipin.com/vue/index/',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
              'x-requested-with': 'XMLHttpRequest'}
    res = json.loads(requests.get(url, headers = header).text)
    empList = res['zpData']['geekList']
    # print('当前页一共{}个人'.format(len(empList)))
    for i in empList:
        name = i['geekCard']['geekName']  # 姓名
        year = i['geekCard']['geekWorkYear']  # 工作年限
        salary = i['geekCard']['salary']    # 薪资待遇
        applyStatusDesc = i['geekCard']['applyStatusDesc']   # 离职状态
        ageDesc = i['geekCard']['ageDesc']   # 年龄
        geekWorks = i['geekCard']['geekWorks']  # 曾经就职
        work = list()
        for j in geekWorks:
            everWork = j['company']
            if '美团' in everWork or '粉象' in everWork:
                work.append(everWork)

        if work == []:
            continue
        print('****************************************************')
        print(name)
        print(year)
        print(salary)
        print(applyStatusDesc)
        print(ageDesc)
        print(work)
        print('****************************************************')

# def getResponse(position, page):
#     url = 'https://www.zhipin.com/wapi/zpitem/web/boss/search/geeks.json?page={}&keywords={}&tag=&city=101010100&experience=-10,20&salary=-1,-1&age=0,30&schoolLevel=-1&applyStatus=-1&degree=201,201&source=1'.format(page, position)
#     header = {'accept': 'application/json, text/plain, */*',
#               'cookie': '__g=-; __l=r=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fboss%2Frecommend&l=%2Fwww.zhipin.com%2Fweb%2Fboss%2Frecommend&g=&s=3&friend_source=0; JSESSIONID=""; _bl_uid=Idk32iChfn5o045pp5nI24pxtj8C; ___gtid=-1955052366; __fid=1cf98cff472f055192d09eb63502fe88; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1607305699,1607388865,1607394982; lastCity=101010100; wt2=6Pbc9s0u2hfS4mts; _bl_uid=F0k5qf7g3gqlmyh7wlty2tRed30g; JSESSIONID=""; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1607413612; __c=1607394982; __a=81815318.1600144826.1607388865.1607394982.197.11.37.59',
#               'referer': 'https://www.zhipin.com/vue/index/',
#               'sec-fetch-dest': 'empty',
#               'sec-fetch-mode': 'cors',
#               'sec-fetch-site': 'same-origin',
#               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
#               'x-requested-with': 'XMLHttpRequest'}
#     res = json.loads(requests.get(url, headers = header).text)
#     # 岗位 ，

def main(position):
    for i in range(1, 31):
        getTotalCount(i)

if __name__ == '__main__':
    position = '产品经理'
    main(position)
