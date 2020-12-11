import gevent
from gevent import monkey,pool
monkey.patch_all()
import requests
import json
import time
import random
import xlsxwriter
import datetime

class saveData(object):
    work = xlsxwriter.Workbook('销售订单压测数据' + datetime.datetime.now().strftime("%m-%d-%H-%M-%S") + '.xlsx')
    sheet1 = work.add_worksheet('sheet1')
    sheet1.write(0,0,'请求总数:')
    sheet1.write(0,1,'时间间隔:')
    sheet1.write(0,2,'发送总请求用时:')
    sheet1.write(0,3,'通过请求次数:')
    sheet1.write(0,4,'请求异常次数:')
    sheet1.write(0,5,'总响应最大时长:')
    sheet1.write(0,6,'总响应最小时长:')
    sheet1.write(0,7,'所有请求累加时长:')
    sheet1.write(0,8,'所有请求结束耗时:')
    sheet1.write(0,9,'平均响应时长:')

    sheet2 = work.add_worksheet('sheet2')
    sheet2.write(0,0,'异常编号')
    sheet2.write(0,1,'异常响应')

    def save(self,num, timeJiange,totalTi,passTi,erroeTi,maxTi,minTi,allResTi,allOverTi,averageTi):
        self.sheet1.write(1,0,num)
        self.sheet1.write(1,1,timeJiange)
        self.sheet1.write(1,2,totalTi)
        self.sheet1.write(1,3,passTi)
        self.sheet1.write(1,4,erroeTi)
        self.sheet1.write(1,5,maxTi)
        self.sheet1.write(1,6,minTi)
        self.sheet1.write(1,7,allResTi)
        self.sheet1.write(1,8,allOverTi)
        self.sheet1.write(1,9,averageTi)
        self.work.close()

    def __del__(self):
        self.work.close()

# 压力测试类
class stressTest(saveData):
    success = 0
    failed = 0
    resTime = []

    def __init__(self):
        self.url = 'https://t4.fsyuncai.com/tmsopenapi/orderReceive/insertSalesOrder'
        self.header = {'Accept': 'application/json',
                       'Content-Type': 'application/json'}
        self.data = {
            "addBillNo": "",
            "addressDetail": "崇文门外大街100",
            "area": "东城区",
            "auditTime": 1603444452000,
            "billAmount": 412.0,
            "billDate": 1603382400000,
            "billType": 19649,
            "city": "北京市",
            "contacter": "1",
            "contacterTel": "1",
            "custCode": "05.02.0013",
            "custId": 6144,
            "custName": "批发客户",
            "custTel": "1",
            "cuttingRequire": "",
            "deliveryBeginDate": 1603598400000,
            "deliveryCategory": 2,
            "deliveryCompany": "京南物流中心",
            "deliveryCompanyId": 257938,
            "deliveryEndDate": 1603616400000,
            "deliveryMethod": 40,
            "incomeAmountType": 2,
            "invoiceProve": "KH",
            "invoiceType": -1,
            "isCarryMaterial": "",
            "isLimit": 18913,
            "isUrgent": 2,
            "latitude": 39.9011824619143,
            "longitude": 116.42632288968875,
            "longitudeAndLatitude": "116.42632288968875,39.9011824619143",
            "makeBillDate": 1603444373000,
            "makerCompany": "小井分公司",
            "makerCompanyId": 198,
            "organizationSource": "",
            "priceType": 918,
            "province": "北京市",
            "relatedRefundNo": "",
            "saleBillNo": "XS35902816",
            "saleCompany": "大兴分公司",
            "saleCompanyId": 116488,
            "saleOrderDetailInsertRequestList": [{
                "categoryId": 1271,
                "isCarryMaterial": 0,
                "isDangerGood": 0,
                "lackNum": 1803.0,
                "organizeNum": 0.0,
                "packageNum": "127根/捆，6米根",
                "position": "大兴6库南",
                "positionId": 708623,
                "product": "Z天谊镀锌管",
                "productAmount": 412.0,
                "productCode": "056930",
                "productMaxEdge": 600.0,
                "productNum": 10.0,
                "productTotalVolume": 0.0,
                "productTotalWeight": 0.0,
                "productUnitVolume": 0.003456,
                "productUnitWeight": 7.04,
                "rejectionMinUnit": 0.0,
                "specModel": "20*2.0",
                "stockLowerLimit": 2000,
                "stockUpperLimit": 1000,
                "unit": "根",
                "unitPrice": 41.2
            }],
            "salerContacter": "1",
            "salerContacterTel": "1",
            "shoppingIdeas": 39742,
            "source": 1,
            "town": "崇文门外街道",
            "transportRequire": "//"
        }

    def begin(self,num,billNo):
        print(num)
        self.data['latitude'] = (random.randint(0,531671) / 100000) + 39.710532
        self.data['longitude'] = (random.randint(0,1149831) / 1000000) + 116.077717
        self.data['longitudeAndLatitude'] = '{},{}'.format((random.randint(0,1149831) / 10000) + 116.077717,(random.randint(0,35701220) / 100000) + 39.710532)
        self.data['saleBillNo'] = billNo
        try:
            res = requests.post(self.url, headers = self.header, data = json.dumps(self.data), timeout = 90)
        except Exception as e:
            print(e)
            self.failed += 1
            self.sheet2.write(self.failed,0,num)
            self.sheet2.write(self.failed,1,str(e))
        else:
            if res.status_code == 200 and '操作成功' in res.text:
                self.success += 1
                self.resTime.append(res.elapsed.total_seconds())
            elif '单据已存在' in res.text:
                print(res.text)
                self.failed += 1
                self.sheet2.write(self.failed,0,num)
                self.sheet2.write(self.failed,1,res.text)
            else:
                print(res.text)
                self.failed += 1
                self.sheet2.write(self.failed,0,num)
                self.sheet2.write(self.failed,1,res.text)

    def __del__(self):
        print('结束！！！！！')
        self.work.close()

def main():
    num = int(input('输入请求次数:'))
    rate = float(input('请求频率(秒/次):'))
    obj = stressTest()
    th = []
    s = time.time()
    global calc
    calc = 0
    l_bill = []
    while calc < num:
        billNo = 'YCXS' + str(int(time.time() * 100000000))[-6:]
        if billNo in l_bill:
            continue
        l_bill.append(billNo)
        t = po.spawn(obj.begin,calc, billNo)
        th.append(t)
        time.sleep(rate)
        calc += 1
    e = time.time()
    print("%d次请求，间隔%d秒,耗时%f秒" % (num,rate,round(e-s,2)))
    gevent.joinall(th)
    e1 = time.time()
    saveobj = saveData()
    if obj.resTime == []:
        obj.resTime.append(0)
    saveobj.save(num,rate,round(e-s,2),obj.success,obj.failed,max(obj.resTime),min(obj.resTime),sum(obj.resTime),round(e1-s,2),(sum(obj.resTime)/len(obj.resTime)))
    print('测试结束:')
    print('请求通过次数:%d' % obj.success)
    print('请求异常次数:%d' % obj.failed)
    print('总响应最大时长:%f' % max(obj.resTime))
    print('总响应最小时长:%f' % min(obj.resTime))
    print('所有请求累加时长:%f' % sum(obj.resTime))
    print('所有请求结束耗时:%f' % round(e1-s,2))
    print('平均响应时长:%f' % (sum(obj.resTime)/len(obj.resTime)))


if __name__ == '__main__':
    po = pool.Pool(10000)
    main()


