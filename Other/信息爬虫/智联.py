import requests
import json

def spider(num, b):
    print('第{}页'.format(b))
    url = 'https://rd5.zhaopin.com/api/rd/chat/recommended?_=1607434285747&x-zp-page-request-id=af88c26bad9b4a1dbac18cd4ba4d94b8-1607434283901-432137&x-zp-client-id=0a4143a8-ccf2-408c-9573-c379388496ae'
    header = {'accept': 'application/json, text/javascript, */*; q=0.01',
              'content-type': 'text/plain',
              'sec-fetch-dest':'empty',
              'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
              'cookie': 'urlfrom=121113803; urlfrom2=121113803; adfbid=0; adfbid2=0; x-zp-client-id=0a4143a8-ccf2-408c-9573-c379388496ae; sts_deviceid=17642101b2319b-032629e96a918-3f6b4b05-2073600-17642101b243a7; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.060000KOIHGPZKYlCCdpFG0KtXhIsV8dP7A0MP4I3eqejuX734ZaYZMgUN67HIO3SRe_edqDfxMIlTgiIOtu66OpG4CaQZfZwy6ZKUmZCseGhYpYNquL8BjyUBZIVtwAHGqaQI-hnjpGQADfV_shZpq39d_b2sbQlc1IOCqIUNOXbKYyBh9sEwF7Hr0UBGyHRZqgTA94GS3zHilMTR_8Ln2GRtCG.7Y_NR2Ar5Od669BCXgjRzeASFDZtwhUVHf632MRRt_Q_DNKnLeMX5Dkgbooo3eQr5gKPwmJCRnTxOoKKsTZK4TPHQ_U3bIt7jHzk8sHfGmEukmnTr59l32AM-YG8x6Y_f3lZgKfYt_QCJamJjArZZsqT7jHzs_lTUQqRHArZ5Xq-dKl-muCyrMWYv0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqd_xKJVgfko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqd_xKJVgfko60ThPv5HD0IgF_gv-b5HDdnWc4nj6vnWT0UgNxpyfqnHfsn1T3PW60UNqGujYknj6knHRLrfKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00pywW5R9awfKWThnqnWnznjT%26ck%3D8059.2.116.342.152.442.147.372%26dt%3D1607426116%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26tpl%3Dtpl_11534_23295_19442%26l%3D1522908627%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526linkType%253D; sajssdk_2015_cross_new_user=1; at=361cb58e3d7f46208965796374154a0d; rt=2819b29a92f84c0593698f8f1c5cd31a; ZP_OLD_FLAG=false; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1607426153; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1607426153; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; zp-route-meta=uid=1091020688,orgid=123436868; login_point=123436868; diagnosis=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221091020688%22%2C%22first_id%22%3A%2217642101bb64e-082320c52fe6a4-3f6b4b05-2073600-17642101bb76b8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22%24device_id%22%3A%2217642101bb64e-082320c52fe6a4-3f6b4b05-2073600-17642101bb76b8%22%7D; isFirstPublish={%22notFirstPublish%22:false}; dywea=95841923.2209176692502485800.1607426369.1607426369.1607426369.1; dywec=95841923; dywez=95841923.1607426369.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; __utmc=269921210; __utma=269921210.1181081369.1607426369.1607426369.1607426369.1; __utmz=269921210.1607426369.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); jobPublicRefresh={%22refreshName%22:%22%E6%97%A0%E5%88%B7%E6%96%B0%22}; promoteGray=; selectedJob-123436868-1091020688=CCL1234368680J40083463716; ssxmod_itna=QuDQYKAKiIPU2aDzxAgYNDk3tS3MDGuDithm77DlEYxA5D8D6DQeGTbRWhTdPdo3eRhfGq0iR5dhP7pjoExek9T4GLDmKDyKjibYoD4RKGwD0eG+DD4DWjx03DoxGABhaTKiODQ40kDmqG2RqNDA4DjWq+4Wktj/dXDxGUxIMGqWqDMD7tD/3htOeDBlen4DYPaYLX/DBQD7w0Bn3iDCr+PAipCp74=fipxAGxbYoqECi4iRYhiDh4WtYmqAied3G+Wl6HxD; ZL_REPORT_GLOBAL={%22jobs%22:{%22recommandActionidShare%22:%2270a5def7-8e9a-4c18-bdd7-cd0452873ba0-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; acw_tc=276082a116074341332173144ee3f88dfa43ce5992fd450345f72160f7d71b; sts_evtseq=1; sts_sid=176428cb249356-0309d0eed34b29-3f6b4b05-2073600-176428cb24a71d'}
    data = {"number":20,
            "jobNumbersIndex":0,
            "resumesIndex":num,
            "jobNumbers":["CCL1234368680J40083463716"],
            "education":"",
            "workYears":"",
            "desiredSalary":"",
            "logTime":"",
            "isUnified":False,
            "searchConditions":""}
    res = json.loads(requests.post(url, headers = header, data = json.dumps(data)).text)
    if res['data'] == []:
        return 0
    for i in res['data']['recommendResumes']:
        name = i['userName']
        age = i['age']
        everWork = i['workExperiences']
        salary = i['preferredUserPurpose']['preferredSalary']['name']

        compL = list()
        for j in everWork:
            comp = j['companyName']
            if '美团' in comp or '粉象' in comp:
                compL.append(comp)
        if not compL == []:
            print('***************************')
            print(name)
            print(age)
            print(salary)
            print(compL)
            jianli = 'https://rd5.zhaopin.com/resume/detail?resumeNo={}_1_1%3B{}%3B{}'.format(i['resumeNumber'], i['resumeK'], i['resumeT'])
            print('简历地址：',jianli)
            print('***************************')

def main():
    b = 1
    for num in range(0,1000,20):
        a = spider(num, b)
        b += 1
        if a==0:
            break

if __name__ == '__main__':
    main()