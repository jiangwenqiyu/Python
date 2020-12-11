import gevent
from gevent import monkey
monkey.patch_all()
import requests
import json
import time
import random
import xlsxwriter

class saveData(object):
    work = xlsxwriter.Workbook('接货单压测数据' + datetime.datetime.now().strftime("%m-%d %H:%M:%S") +'.xlsx')
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
        self.url = 'http://t4.fsyuncai.com/tmsopenapi/orderReceive/insertReceiveOrder'
        self.header = {'Accept': 'application/json',
                       'Content-Type': 'application/json'}
        self.data = {
            "addressDetail": "北京市-北京市-丰台区-花乡(地区)乡京开辅路新发地甘肃厅",
            "addressSort": "分类1",
            "addressSortId": 1,
            "addressTel": "15677146777",
            "area": "丰台区",
            "auditTime": 1603429668753,
            "billAmount": 15679.68,
            "billDate": 1603382400000,
            "billType": 39734,
            "city": "北京市",
            "goodFunds": "需带回资料",
            "goodHandleMethod": 18910,
            "isBackMaterial": 2,
            "isBackMoney": 0,
            "isLimit": 2,
            "isTax": 2,
            "latestDeliveryTime": 1603533600000,
            # 南 116.378972,39.710532
            # 北 116.236393,40.242203
            # 西 116.077717,39.900323
            # 东 117.227548,40.09312
            "latitude": (random.randint(0,531671) / 100000) + 39.710532,
            "longitude": (random.randint(0,1149831) / 1000000) + 116.077717,
            "maker": "石凤刚",
            "makerBillDate": 1603429665000,
            "makerCompany": "北京结算中心",
            "makerCompanyId": 756726,
            "makerContacter": "吴静",
            "makerContacterId": 0,
            "makerContacterTel": "14566136777",
            "makerId": 16297,
            "money": 0.0,
            "pickCompany": "京南物流中心",
            "pickCompanyId": 257938,
            "province": "北京市",
            "purchaseBillNo": "CG-1501090",
            "receiveBillNo": "JHD-YC-0001",
            "receiveOrderDetailInsertRequestList": [{
                "categoryId": 1002,
                "isDangerGood": 2,
                "pickingRequire": "",
                "position": "大兴7库F",
                "positionId": 128853,
                "product": "Z博世热风枪L",
                "productAmount": 10278.72,
                "productCode": "004183",
                "productMaxEdge": 27.5,
                "productNum": 16.0,
                "productUnitVolume": 0.007185,
                "productUnitWeight": 1.13,
                "specModel": "GHG20-63(2000W)",
                "unit": "把",
                "unitPrice": 642.42
            },
                {
                    "categoryId": 1002,
                    "isDangerGood": 2,
                    "pickingRequire": "",
                    "position": "大兴7库F",
                    "positionId": 128853,
                    "product": "Z博世热风枪L",
                    "productAmount": 5400.96,
                    "productCode": "044374",
                    "productMaxEdge": 27.5,
                    "productNum": 16.0,
                    "productUnitVolume": 0.007185,
                    "productUnitWeight": 0.97,
                    "specModel": "GHG16-50(1600W)",
                    "unit": "台",
                    "unitPrice": 337.56
                }],
            "remark": "带运费100",
            "supplier": "Z北京林华伟业机电设备有限公司D(博世电动工具)",
            "supplierId": 209001,
            "supplierTel": "010-83690993 ",
            "town": "花乡(地区)乡",
            "updateDateReason": ""
        }

    def begin(self,num):
        print(num)
        self.data['latitude'] = (random.randint(0,531671) / 100000) + 39.710532
        self.data['longitude'] = (random.randint(0,1149831) / 1000000) + 116.077717
        self.data['receiveBillNo'] = 'YCJHD' + str(int(time.time() * 100000))[-5:]
        try:
            res = requests.post(self.url, headers = self.header, data = json.dumps(self.data))
        except Exception as e:
            print(e)
            self.failed += 1
            self.sheet2.write(self.failed,0,num)
            self.sheet2.write(self.failed,1,str(e))
        else:
            if res.status_code == 200 and '操作成功' in res.text:
                self.success += 1
                self.resTime.append(res.elapsed.total_seconds())
            else:
                print(res.text)
                self.failed += 1
                self.sheet2.write(self.failed,0,num)
                self.sheet2.write(self.failed,1,res.text)

def main():
    num = int(input('输入请求次数:'))
    rate = float(input('请求频率(秒/次):'))
    obj = stressTest()
    th = []
    s = time.time()
    for i in range(num):
        t = gevent.spawn(obj.begin,i)
        th.append(t)
        time.sleep(rate)
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
    main()


