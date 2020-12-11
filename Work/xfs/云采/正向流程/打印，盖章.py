import requests
import json
import tkinter as tk
from tkinter.messagebox import *

class BasicInfo(object):
    userid = 16297
    # host = 'http://111.200.196.1:8012'    # t2  66103261301
    host = 'http://192.168.0.121:8012'    # t4
    FID = 0

# 打印
class printTicket(BasicInfo):
    # 查询订单id
    def queryID(self, billNo):
        url = '{}/Sales/SalePageList'.format(self.host)
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        data = {
            "webParameterList": [{
                "logic": -1,
                "leftBracket": 0,
                "field": "fbillid",
                "condition": 0,
                "value": billNo,
                "rightBracket": 0,
                "fieldType": 0
            }],
            "currentPage": 1,
            "pageSize": 200,
            "printType": 0,
            "fcompanyid": 12,
            "userid": self.userid,
            "send_department": 756674,
            "TipSql": "",
            "send_department_id": 0
        }
        res = json.loads(requests.post(url, headers = header, data = json.dumps(data), verify = False).text)
        BasicInfo.FID = int(res['Data']['Result'][0]['FID'])
        print(self.FID)
        # print(res)
        return int(res['Data']['Result'][0]['FID'])

    def PrintSale(self, billNo):
        for i in range(1,3):
            url = '{}/Sales/PrintSale'.format(self.host)
            header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
            data = {'id':self.queryID(billNo),
                    'userid':self.userid,
                    'ordertype':str(i)}
            res = requests.post(url, headers = header, data = data, verify = False).text
            print(res)

# 盖章
class Stamp(BasicInfo):
    def stamp(self, FBillId):
        url = '{}/Sales/Check_SaleStamp'.format(self.host)
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        data = [{
            "Fid": self.FID,
            "FBillId": FBillId,
            "Receivables_no": "",
            "Advance_no": "",
            "Com_Receivables_no": "",
            "Com_Advance_no": "",
            "Com_Payable_no": "",
            "UnReceivables_no": "",
            "Seal_UserId": self.userid
        }]
        print(self.FID)
        res = requests.post(url, headers = header, data = json.dumps(data)).text
        print(res)

def dayin(bill):
    try:
        obj = printTicket()
        obj.PrintSale(bill)
        showinfo('成功', message= '打印成功')
    except Exception as e:
        showerror('错误', message=str(e))

def gaizhang(bill):
    try:
        Stamp().stamp(bill)
        showinfo('成功', message= '盖章成功')
    except Exception as e:
        showerror('错误', message=str(e))

if __name__ == '__main__':
    gui = tk.Tk()
    en = tk.Entry(gui, font = 10)
    en.grid()
    bt1 = tk.Button(gui, text = '打印',command = lambda:dayin(en.get()))
    bt2 = tk.Button(gui, text = '盖章',command = lambda:gaizhang(en.get()))
    bt1.grid()
    bt2.grid()
    gui.mainloop()