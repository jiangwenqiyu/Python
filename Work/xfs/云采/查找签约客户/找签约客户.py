import requests
import json

def queryInvoice(customerId):
    url = 'https://t2.fsyuncai.com/api/admin/acontract/invoice/getInvoice.jhtml'
    header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Cookie': 'cityCode=110100; provinceCode=110000; wareHouseCode=1; UM_distinctid=1760cbc1c0834-0671807d53ab1c-3f6b4b05-15f900-1760cbc1c096f2; registerSource=20; goback=; CNZZDATA1274765129=1982007485-1606531424-https%253A%252F%252Ft2.fsyuncai.com%252F%7C1606697860; Hm_lvt_47bc68128fb7e2190a5f2966d6a30000=1606531423,1606699047; Hm_lpvt_47bc68128fb7e2190a5f2966d6a30000=1606699047; m_tk=80f3Ae8DrWSIhQwxhk6B7XdvLv+A3RqH82UF8Hl+eAVAsFPwOPzp1mcveRoASA9EbGP+pjEmUdD9I%2FLsAf95191L9svqoZ1Tiic5Saz9ij82yvjex1XaOBWCGBID8LZy7XDfSaISH1DUtjS%2FbDPW6uk; loginData=%7B%22tokenID%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDY4NzE4NTIzNzAsInBheWxvYWQiOiJ7XCJkZXBhcnRtZW50XCI6bnVsbCxcInJvbGVcIjpudWxsLFwicGFnZVwiOntcInNob3dDb3VudFwiOjUwMDAsXCJ0b3RhbFBhZ2VcIjowLFwidG90YWxSZXN1bHRcIjowLFwiY3VycmVudFBhZ2VcIjowLFwiY3VycmVudFJlc3VsdFwiOjAsXCJlbnRpdHlPckZpZWxkXCI6ZmFsc2UsXCJwYWdlU3RyXCI6XCJcIixcInBkXCI6e30sXCJ1c2VyX0lEXCI6MCxcImRlcGFydG1lbnRfSURcIjowfSxcInJvbGVMaXN0XCI6bnVsbCxcInN0YXR1c1wiOlwiMFwiLFwidXNlcl9JRFwiOjM0MCxcInVzZXJuYW1lXCI6XCJqaWFuZ3ljXCIsXCJuYW1lXCI6XCLlp5zlvabovrBcIixcImRlcGFydG1lbnRfSURcIjpudWxsLFwibnVtYmVyXCI6XCIxMDAwNTc0NFwiLFwiZW5cIjpudWxsLFwiYmlhbm1hXCI6bnVsbCxcImVudHJ5X1RJTUVcIjpudWxsLFwicGFzc3dvcmRcIjpudWxsLFwicGhvbmVcIjpudWxsLFwiZW1haWxcIjpudWxsLFwicmlnaHRzXCI6bnVsbCxcImNyZWF0X1RJTUVcIjpudWxsfSJ9.EA9btx6yxu3AKKfuJMNFCbsfHGt4eoyopb_1euVQpks%22%2C%22roleList%22%3A%5B32%5D%2C%22department%22%3A%7B%22target%22%3Anull%2C%22department%22%3Anull%2C%22subDepartment%22%3Anull%2C%22hasDepartment%22%3Afalse%2C%22treeurl%22%3Anull%2C%22department_ID%22%3Anull%2C%22department_NAME%22%3Anull%2C%22bianma%22%3Anull%2C%22parent_ID%22%3A0%2C%22p_BIANMA%22%3Anull%2C%22max_NUM%22%3Anull%7D%2C%22user%22%3A%7B%22department%22%3Anull%2C%22role%22%3Anull%2C%22page%22%3A%7B%22showCount%22%3A5000%2C%22totalPage%22%3A0%2C%22totalResult%22%3A0%2C%22currentPage%22%3A0%2C%22currentResult%22%3A0%2C%22entityOrField%22%3Afalse%2C%22pageStr%22%3A%22%22%2C%22pd%22%3A%7B%7D%2C%22user_ID%22%3A0%2C%22department_ID%22%3A0%7D%2C%22roleList%22%3Anull%2C%22user_ID%22%3A340%2C%22username%22%3A%22jiangyc%22%2C%22name%22%3A%22%E5%A7%9C%E5%BD%A6%E8%BE%B0%22%2C%22department_ID%22%3Anull%2C%22number%22%3A%2210005744%22%2C%22password%22%3Anull%2C%22phone%22%3Anull%2C%22email%22%3Anull%2C%22bianma%22%3Anull%2C%22entry_TIME%22%3Anull%2C%22status%22%3A%220%22%2C%22rights%22%3Anull%2C%22creat_TIME%22%3Anull%2C%22en%22%3Anull%7D%7D; user_id=340; Hm_lvt_080836300300be57b7f34f4b3e97d911=1606531147,1606699051; Hm_lpvt_080836300300be57b7f34f4b3e97d911=1606699052; memberId=171200; token=33e70d31ad312bbd28b5ada56d0b4e6c; loginAccount=jycsanquan001; accountType=10; lgdomain=t2; mCustomerId=359; customerCode=01.01.0130; customerId=CN00001842; customerType=20; dialogStatus=6; CNZZDATA1274763055=1599185406-1606531959-https%253A%252F%252Ft2.fsyuncai.com%252F%7C1606697882; Hm_lvt_2c8366b03de5b5325b2e73db7fab74e5=1606531960,1606699062; fullPath=/vip/category/982_3.html; Hm_lpvt_2c8366b03de5b5325b2e73db7fab74e5=1606702694'}
    data = {'customerId': customerId,
            'invoiceSource': '20'}
    res1 = json.loads(requests.post(url, headers = header, data = data).text)
    data['invoiceSource'] = '10'
    res2 = json.loads(requests.post(url, headers = header, data = data).text)
    if res1['data'] == [] and res2['data'] == []:
        pass
    else:
        idList.append(customerId)

def getAllId(page, belongGroupId):
    url = 'https://t2.fsyuncai.com/api/admin/acontract/approval/querySignCustomerTable.jhtml'
    header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Cookie': 'cityCode=110100; provinceCode=110000; wareHouseCode=1; UM_distinctid=1760cbc1c0834-0671807d53ab1c-3f6b4b05-15f900-1760cbc1c096f2; registerSource=20; goback=; CNZZDATA1274765129=1982007485-1606531424-https%253A%252F%252Ft2.fsyuncai.com%252F%7C1606697860; Hm_lvt_47bc68128fb7e2190a5f2966d6a30000=1606531423,1606699047; Hm_lpvt_47bc68128fb7e2190a5f2966d6a30000=1606699047; m_tk=80f3Ae8DrWSIhQwxhk6B7XdvLv+A3RqH82UF8Hl+eAVAsFPwOPzp1mcveRoASA9EbGP+pjEmUdD9I%2FLsAf95191L9svqoZ1Tiic5Saz9ij82yvjex1XaOBWCGBID8LZy7XDfSaISH1DUtjS%2FbDPW6uk; loginData=%7B%22tokenID%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDY4NzE4NTIzNzAsInBheWxvYWQiOiJ7XCJkZXBhcnRtZW50XCI6bnVsbCxcInJvbGVcIjpudWxsLFwicGFnZVwiOntcInNob3dDb3VudFwiOjUwMDAsXCJ0b3RhbFBhZ2VcIjowLFwidG90YWxSZXN1bHRcIjowLFwiY3VycmVudFBhZ2VcIjowLFwiY3VycmVudFJlc3VsdFwiOjAsXCJlbnRpdHlPckZpZWxkXCI6ZmFsc2UsXCJwYWdlU3RyXCI6XCJcIixcInBkXCI6e30sXCJ1c2VyX0lEXCI6MCxcImRlcGFydG1lbnRfSURcIjowfSxcInJvbGVMaXN0XCI6bnVsbCxcInN0YXR1c1wiOlwiMFwiLFwidXNlcl9JRFwiOjM0MCxcInVzZXJuYW1lXCI6XCJqaWFuZ3ljXCIsXCJuYW1lXCI6XCLlp5zlvabovrBcIixcImRlcGFydG1lbnRfSURcIjpudWxsLFwibnVtYmVyXCI6XCIxMDAwNTc0NFwiLFwiZW5cIjpudWxsLFwiYmlhbm1hXCI6bnVsbCxcImVudHJ5X1RJTUVcIjpudWxsLFwicGFzc3dvcmRcIjpudWxsLFwicGhvbmVcIjpudWxsLFwiZW1haWxcIjpudWxsLFwicmlnaHRzXCI6bnVsbCxcImNyZWF0X1RJTUVcIjpudWxsfSJ9.EA9btx6yxu3AKKfuJMNFCbsfHGt4eoyopb_1euVQpks%22%2C%22roleList%22%3A%5B32%5D%2C%22department%22%3A%7B%22target%22%3Anull%2C%22department%22%3Anull%2C%22subDepartment%22%3Anull%2C%22hasDepartment%22%3Afalse%2C%22treeurl%22%3Anull%2C%22department_ID%22%3Anull%2C%22department_NAME%22%3Anull%2C%22bianma%22%3Anull%2C%22parent_ID%22%3A0%2C%22p_BIANMA%22%3Anull%2C%22max_NUM%22%3Anull%7D%2C%22user%22%3A%7B%22department%22%3Anull%2C%22role%22%3Anull%2C%22page%22%3A%7B%22showCount%22%3A5000%2C%22totalPage%22%3A0%2C%22totalResult%22%3A0%2C%22currentPage%22%3A0%2C%22currentResult%22%3A0%2C%22entityOrField%22%3Afalse%2C%22pageStr%22%3A%22%22%2C%22pd%22%3A%7B%7D%2C%22user_ID%22%3A0%2C%22department_ID%22%3A0%7D%2C%22roleList%22%3Anull%2C%22user_ID%22%3A340%2C%22username%22%3A%22jiangyc%22%2C%22name%22%3A%22%E5%A7%9C%E5%BD%A6%E8%BE%B0%22%2C%22department_ID%22%3Anull%2C%22number%22%3A%2210005744%22%2C%22password%22%3Anull%2C%22phone%22%3Anull%2C%22email%22%3Anull%2C%22bianma%22%3Anull%2C%22entry_TIME%22%3Anull%2C%22status%22%3A%220%22%2C%22rights%22%3Anull%2C%22creat_TIME%22%3Anull%2C%22en%22%3Anull%7D%7D; user_id=340; Hm_lvt_080836300300be57b7f34f4b3e97d911=1606531147,1606699051; Hm_lpvt_080836300300be57b7f34f4b3e97d911=1606699052; memberId=171200; token=33e70d31ad312bbd28b5ada56d0b4e6c; loginAccount=jycsanquan001; accountType=10; lgdomain=t2; mCustomerId=359; customerCode=01.01.0130; customerId=CN00001842; customerType=20; dialogStatus=6; CNZZDATA1274763055=1599185406-1606531959-https%253A%252F%252Ft2.fsyuncai.com%252F%7C1606697882; Hm_lvt_2c8366b03de5b5325b2e73db7fab74e5=1606531960,1606699062; fullPath=/vip/category/982_3.html; Hm_lpvt_2c8366b03de5b5325b2e73db7fab74e5=1606702694'}
    data = {'customerId':'',
            'customerName':'',
            'belongGroupId': belongGroupId,
            'isEnter': '20',         # 未入住
            'operateManagerId':'',
            'belongSaleDirectorId':'',
            'pageNum': page,
            'pageSize': 50,
            'customerType':'',
            'customerGrade':'',
            'isRestrict':'',
            'limitType':'',
            'warehouseCode': -1,
            'organizationIds': '18,29,30,31,32,34,35,36,37,59,60,61,62,63,65,66,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,105,106,107,108,109,110,111,112,113,115,116,118,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168',
            'salesSupervisorUserIds':'',
            'startEnterTime':'',
            'endEnterTime':''}
    res = json.loads(requests.post(url, headers = header, data = data).text)
    for i in res['list']['result']:
        cusid = i['customer_id']
        queryInvoice(cusid)


def main():
    global idList
    idList = list()
    getAllId(1, '29')
    print(idList)


if __name__ == '__main__':
    main()