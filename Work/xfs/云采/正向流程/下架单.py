import requests
import json

class basicInfo():
    host = 'http://192.168.0.104:8082'   # t4

# 查询、生成下架单
class DownOut(basicInfo):
    billnum = ''
    idsList = list()
    numList = list()
    comsoId = ''
    fidList = list()

    # 下架  1.查询有几个下架单  2.逐个下架
    def __init__(self, billnum):
        DownOut.billnum = billnum
        DownOut.idsList = list()
        DownOut.numList = list()
        DownOut.comsoId = ''
        DownOut.fidList = list()
        self.actDown()

    # 查询订单  ids，num， comsoId
    def queryNum(self):
        print('查询订单商品信息')
        url = '{}/wms/pickKanban/listComsoBillByPickTaskAssign'.format(self.host)
        header = {'Content-Type': 'application/json;charset=UTF-8',
                  'oldclient': '0'}
        data = {
            "filter": [{
                "logic": -1,
                "leftBracket": 0,
                "field": "c.fdownno",
                "condition": 0,
                "value": self.billnum,
                "rightBracket": 0,
                "fieldType": 0
            }],
            "fixedCondition": "and c.fisyxjh=1 and c.fcompanyid=257938 and c1.fstockid in(128850,128851,128852,128853,128854,128855,154916,451841,525616,649627,708622,708623,708624,756671,756678,756679,756680,756681,756695,756699,756700,756701,756702,756703,756704,756705,756706,756707,756724,756763,756771,756777,756826,756892,756914)"
        }
        res = json.loads(requests.post(url, headers = header, data = json.dumps(data)).text)
        if res['data'] == None:
            raise Exception("单据未到达鸿鹄！")
        # 下架id列表
        DownOut.comsoId = res['data'][0]['comsoId']
        for i in res['data']:
            self.idsList.append(i['entryId'])
            self.numList.append(i['qty'])


    # 2.拿到ids，进行下架
    def actDown(self):
        idsList = self.queryNum()
        print('开始下架')
        url = '{}/wms/service/wmsService'.format(self.host)
        header = {'Content-Type': 'text/xml; charset=utf-8',
                  'SOAPAction': '""',
                  'Expect': '100-continue'}
        for ids in self.idsList:
            data = '''<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><getSaleReturnDownScheme xmlns="http://xfs.webservice.wms.com"><ids>{}</ids><isAutoPrint>0</isAutoPrint></getSaleReturnDownScheme></soap:Body></soap:Envelope>'''.format(ids)
            res = requests.post(url, headers = header, data = data).text
            print(res)
        print('下架成功')
        print('************************************************************************')
        print('************************************************************************')

# 分配拣货人
class assignTask(DownOut):
    def __init__(self):
        self.queryTask()
        self.assign()

    # 1. 查询拣货任务分配
    def queryTask(self):
        print('查询拣货任务分配')
        url = '{}/wms/pickKanban/listComsoStoragedownByPickTaskAssign'.format(self.host)
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        data = {
            "filter": [],
            "fixedCondition": "and t.fparentid in ({}) and t.fcompanyid = 257938 and t.fstockid in (128850,128851,128852,128853,128854,128855,154916,451841,525616,649627,708622,708623,708624,756671,756678,756679,756680,756681,756695,756699,756700,756701,756702,756703,756704,756705,756706,756707,756724,756763,756771,756777,756826,756892,756914)".format(self.comsoId)
        }
        res = json.loads(requests.post(url, headers = header, data = json.dumps(data)).text)
        # print(res)
        for i in res['data']:
            DownOut.fidList.append(i['storagedownId'])

    # 需要   storagedownId  也就是fidList
    def assign(self):
        print('开始分配拣货人', self.fidList)
        url = '{}/wms/service/wmsService'.format(self.host)
        header = {'Content-Type': 'text/xml; charset=utf-8'}
        for ids in self.fidList:
            data = '''<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <soap:Body><updateJHuser xmlns="http://xfs.webservice.wms.com">
            <ids>{}</ids>
            <userid>14310</userid>
            <fstateid>0</fstateid>
            </updateJHuser></soap:Body></soap:Envelope>'''.format(ids)
            res = requests.post(url, headers = header, data = data).text
            print(res)
        print('拣货人分配完成')
        print('************************************************************************')
        print('************************************************************************')

# 电脑下架
class computerDown(DownOut):
    def __init__(self):
        self.cpmputer()

    # 2.进行电脑下架
    def cpmputer(self):
        datalist = list()
        print('开始电脑下架')
        for i in range(len(self.idsList)):
            temp = dict()
            temp['fid'] = self.fidList[i]
            temp['frealqty'] = self.numList[i]
            temp['fsourceid'] = self.idsList[i]
            temp['fsourcetype'] = 18
            temp['fbillid'] = self.billnum
            datalist.append(temp)

        databody = str(datalist)
        url = '{}/wms/service/wmsService'.format(self.host)
        header = {'Content-Type': 'text/xml; charset=utf-8'}
        data = '''<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <soap:Body>
        <executeDownByPc xmlns="http://xfs.webservice.wms.com">
        <userid>16297</userid>
        <data>{}</data>
        <fcarno /><fhuserid>14705</fhuserid>
        <companyid>257938</companyid>
        </executeDownByPc></soap:Body></soap:Envelope>'''.format(databody)
        res = requests.post(url, headers = header, data = data).text
        print(res)
        print(databody)

# 审核
def check():
    url = ''
    header = {}
    data = '''<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body><saveBill xmlns="http://xfs.webservice.wms.com">
    <data>{"billdata":"
    {\"fid\":0,
    \"fdate\":\"2020-12-05T00:00:00\",
    \"fbillid\":\"\",
    \"ftype\":18,
    \"fcustomerid\":854841,
    \"fdeptid\":857146,
    \"femployee\":225503,
    \"fstateid\":0,
    \"fcheckid\":0,
    \"fdownid\":0,
    \"fdownno\":\"\",
    \"fcreateuserid\":0,
    \"fcompanyid\":257938,
    \"fsoid\":\"\",
    \"delivery_corp_legal_id\":11,
    \"sale_method_id\":51,
    \"sale_corp_id\":756779,
    \"sale_corp_legal_id\":11,
    \"invoice_customer_id\":1,
    \"fuserid\":16297,
    \"ftime\":\"2020-12-05T14:53:55\",
    \"fnote\":\"\",
    \"is_online_order\":1,
    \"collection_type\":2}",
    "entrydata":"[{\"fid\":0,
    \"fentryid\":1,
    \"fitemid\":45792,
    \"funit\":1956,
    \"fqty\":1.0,
    \"fstockid\":128854,
    \"fsrcbilltype\":4,
    \"fsrcbillid\":\"66103302101\",
    \"fscrbillfid\":35904708,
    \"fscrbillfentryid\":2,
    \"fparentid\":0,
    \"fprice\":1.98,
    \"famt\":1.98,
    \"fstockname\":\"大兴9库K\",
    \"fsourceid\":20513969,
    \"fsourcetype\":4,
    \"fcb\":1.47,
    \"fkptype\":4,
    \"fkpbillid\":\"66103302101\",
    \"fkpfid\":35904708,
    \"fkpentryid\":\"2\",
    \"fjhqty\":1.0,
    \"fckqty\":0.0,
    \"relationbill_entryid\":180656004,
    \"tax_rate\":0.13,
    \"tax_free_price\":1.752212},
    {\"fid\":0,
    \"fentryid\":2,
    \"fitemid\":11714,
    \"funit\":1972,
    \"fqty\":2.0,
    \"fstockid\":708622,
    \"fsrcbilltype\":4,
    \"fsrcbillid\":\"66103302101\",
    \"fscrbillfid\":35904708,
    \"fscrbillfentryid\":1,
    \"fparentid\":0,
    \"fprice\":88.4,
    \"famt\":176.8,
    \"fstockname\":\"大兴9库C\",
    \"fsourceid\":20513968,
    \"fsourcetype\":4,
    \"fcb\":73.47,
    \"fkptype\":4,
    \"fkpbillid\":\"66103302101\",
    \"fkpfid\":35904708,
    \"fkpentryid\":\"1\",
    \"fjhqty\":2.0,
    \"fckqty\":0.0,
    \"relationbill_entryid\":180656003,
    \"tax_rate\":0.13,
    \"tax_free_price\":78.230089}]",
    "checkstate":1,
    "fbillid":0,
    "userid":16297,
    "fmoduleid":0,
    "type":"SaleOutStockController",
    "flowStatus":10,
    "companyId":0}
    </data></saveBill></soap:Body></soap:Envelope>'''

DownOut('66103305301')  # 查询、生成下架单
assignTask()            # 分配拣货人
computerDown()          # 电脑下架
