import requests
import json
import time
import datetime
import tkinter as tk
import tkinter.ttk as ttk
import threading
from tkinter.messagebox import *
import configparser
import os
import sys

# 销售订单
def makeOrder(x,y,li_a,li_b, num,senddate,sendtime,stockCode):
    try:
        global total
        url = 'http://192.168.0.121:8012/Sales/SaveSale'
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        if orderType.get() == '物流配送':
            data = {"fthfs":39742,"fdeptid":419509,"femployee":469415,"finfor":"","faffiliated":382853,"faffiliatlinkman":"测试联系人","faffiliatphone":"测试电话","fbillid":"","fdate":"2020-09-02 00:00:00","fkhxffs":18864,"fcustomerid":6144,"invoiceunit":1,"fpricetype":918,"fsaletype":51,"fnewcustomername":"测试客户名称","fcustomerlinkman":"测试联系人","fcustomerphone":"测试电话","deliveryarea":"北京市北京市大兴区林校路街道","fdeliveryadd":"市场街205号","fsfxx":18914,"senttype":40,"fsfjj":2,"fkfpyj":15600,"ffpdw":"测试单位","fisgcxk":18913,"ftakenote":"测试资料","frlnote":"测试让利","fycnote":"测试异常","fnote":"不给客户任何票据","fordertype":19649,"receiptno":"","fhth":"测试合同","selfoperated":18914,"fbrid":12,"fsenddatetime":"2020-09-03 08:00:00","flastsenddatetime":"2020-09-03 17:00:00","fid":0,"fdownid":0,"faddsub":18920,"flowuser":"","flownote":"","flowcbuser":"","finvoicetype":0,"fpayeetype":0,"fdownno":"","ftype":2,"fcustomernumber":"","fpricetypename":"","fsaletypename":"","fempnumber":"","fdepnumer":"","finvoicetypename":"","fpayeetypename":"","fsoncompanynumber":"","fkfpyjname":"","fkhxffsname":"","fthfsname":"","foperationtypename":"","fdirectoridname":"","foperationtype":18918,"fstatename":"","fk3billid":"","fybillid":"","fiskf":"","faddsubname":"","fnodh":"","fisdh":0,"fnodhck":"","fxsgsid":19583,"fxsgsname":"","fscore":0,"fisgcxkname":"","fordertypename":"配送订单","ftj":0,"ftjrole":0,"fqu":"大兴区","fcompanyid":12,"ftjname":"","fthsqbillid":"","fsfxxname":"","fsoid":"","fempname":"","fstateid":0,"fcustomername":"","fdepname":"","fsoncompanyname":"网销事业部","jlzhprint":None,"jlzhprintname":"","pid":0,"senttypename":"","bill_count":1,"bill_amt":200.0,"sale_ordertype":2,"send_department_name":"","large_area_id":100,"legal_person_id":11,"corporation_id":116488,"department_id":128842,"receivable_dep_id":0,"return_type_name":"","advance_receipt_date":"","advance_receipt_id":"","advance_receipt_billno":"","return_status":0,"disp_status":0,"status":0,"send_department":stockCode,"return_type":39801,"invoiceunitname":"","makebillcompanyid":116488,"selfoperatedname":"","agencysales":18914,"agencysalesname":"","collecting_company":0,"return_reason_id":0,"proxysale_companyid":0,"is_distributor":0,"distributor_amt":200.0,"proxysale_companyname":"","isyuncai":"","customer_address_id":0,"township":"林校路街道","province_id":43543,"city_id":43543,"area_id":39529,"street_id":237,"logistics_note":"不给客户任何票据","other_note":"","item_note":"","waitorganize_details":"测试详情","cutting_require":"测试要求","logistics_warehouse":stockCode,"map_restrictions":18914,"fuserid":21724,"fusername":"陈化淳","fdirectorid":0,"fcheckid":"","fcheckname":"","fchecktime":"","fbjdno":"","pno":"","longest_edge":"","volume":"","weight":"","fjwd":"116.34862844613083,39.732554820386085","platform":20,"is_abnormal":0,"page_count":1}
        else:
            data = {"fthfs":39739,"fdeptid":377819,"femployee":469415,"finfor":"","faffiliated":382853,"faffiliatlinkman":"","faffiliatphone":"","fbillid":"","fkhxffs":18864,"fcustomerid":6144,"invoiceunit":1,"fpricetype":918,"fsaletype":51,"fnewcustomername":"123123","fcustomerlinkman":"123123123","fcustomerphone":"123123123","deliveryarea":"北京市北京市大兴区林校路街道","fdeliveryadd":"市场街205号","fsfxx":18914,"senttype":10,"fsfjj":0,"fkfpyj":15600,"ffpdw":"123123","fisgcxk":18913,"ftakenote":"","frlnote":"13123","fycnote":"123123123","fnote":"","fordertype":33790,"receiptno":"","fhth":"123123","selfoperated":18914,"fid":0,"fbrid":12,"fdownid":0,"faddsub":18920,"finvoicetype":0,"fpayeetype":0,"fdownno":"","ftype":1,"fcustomernumber":"","fpricetypename":"","flowuser":"","fsaletypename":"","flownote":"","fempnumber":"","flowcbuser":"","fdepnumer":"","finvoicetypename":"","fpayeetypename":"","fsoncompanynumber":"","fkfpyjname":"","fkhxffsname":"","fthfsname":"","foperationtypename":"","fdirectoridname":"","foperationtype":18918,"fstatename":"","fk3billid":"","fybillid":"","fiskf":"","faddsubname":"","fnodh":"","fisdh":0,"fnodhck":"","fxsgsid":19583,"fxsgsname":"","fscore":0,"fisgcxkname":"","fordertypename":"","ftj":0,"ftjrole":0,"fqu":"大兴区","ftjname":"","fthsqbillid":"","fsfxxname":"","fsoid":"","fcompanyid":12,"fempname":"","fstateid":0,"fcustomername":"","fdepname":"","fsoncompanyname":"","jlzhprint":None,"jlzhprintname":"","pid":0,"senttypename":"","bill_count":1,"bill_amt":200.0,"sale_ordertype":1,"send_department_name":"","large_area_id":100,"legal_person_id":11,"corporation_id":116488,"department_id":128842,"receivable_dep_id":0,"return_type_name":"","advance_receipt_date":"","advance_receipt_id":"","advance_receipt_billno":"","return_status":0,"disp_status":0,"status":0,"send_department":257938,"return_type":39801,"invoiceunitname":"","makebillcompanyid":116488,"selfoperatedname":"","agencysales":18914,"agencysalesname":"","collecting_company":0,"return_reason_id":0,"proxysale_companyid":0,"is_distributor":0,"distributor_amt":200.0,"proxysale_companyname":"","isyuncai":"","customer_address_id":0,"township":"林校路街道","province_id":43543,"city_id":43543,"area_id":39529,"street_id":237,"logistics_note":"","other_note":"","item_note":"","waitorganize_details":"","cutting_require":"123213123","logistics_warehouse":257938,"map_restrictions":18914,"fuserid":21724,"fusername":"陈化淳","fdirectorid":0,"fcheckid":"","fcheckname":"","fchecktime":"","fbjdno":"","pno":"","longest_edge":"","volume":"","weight":"","fjwd":"116.34862844613083,39.732554820386085","platform":20,"is_abnormal":0,"page_count":1}
        # 时间参数
        current = datetime.datetime.now()
        data["fdate"] = current.strftime('%Y-%m-%d 00:00:00')
        if senddate == '明天':
            date = 1
        elif senddate == '后天':
            date = 2
        elif senddate == '大后天':
            date = 3

        if sendtime == '白天送':
            data["fsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 08:00:00')
            data["flastsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 17:00:00')
        elif sendtime == '上午送':
            data["fsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 08:00:00')
            data["flastsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 12:00:00')
        elif sendtime == '下午送':
            data["fsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 12:00:00')
            data["flastsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 17:00:00')
        elif sendtime == '夜间送':
            data["fsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 17:00:00')
            data["flastsenddatetime"] = (current + datetime.timedelta(days=int(date))).strftime('%Y-%m-%d 23:59:59')
        else:
            print('输入错误！')
            raise Exception('输入错误')

        data["ftime"] = current.strftime('%Y-%m-%d %H:%M:%S')
        # 定位参数
        data["faffiliatphone"] = '11111111111'
        data["fsheng"] = province_e.get()
        data["fshi"] = city_e.get()
        data["fqu"] = district_e.get()
        data["township"] = area_e.get()
        data["deliveryarea"] = province_e.get() + city_e.get() + district_e.get()
        data["fdeliveryadd"] = area_e.get()
        data["fjwd"] = str(x) + ',' + str(y)
        # 商品参数
        li = []
        price_li = []
        for i in range(len(li_a)):
            ware = {
                "fitemid":int(li_a[i]["FITEMID"]),
                "fnumber":li_a[i]["FNUMBER"],
                "fname":li_a[i]["FNAME"],
                "fmodel":li_b[i]["DataObj"][0]["FMODEL"],
                "funit": li_b[i]["DataObj"][0]["FUNIT"],
                "funit1name": li_b[i]["DataObj"][0]["FUNIT1NAME"],
                "fprice": li_b[i]["DataObj"][0]["FPRICE"],
                "fsysprice": li_b[i]["DataObj"][0]["FSYSPRICE"],
                "fstockid": li_b[i]["DataObj"][0]["FSTOCKID"],
                "fstockname": li_b[i]["DataObj"][0]["FSTOCKNAME"],
                "fjzsl": li_b[i]["DataObj"][0]["FJZSL"],
                "fmin": li_b[i]["DataObj"][0]["FMIN"],
                "fmax": li_b[i]["DataObj"][0]["FMAX"],
                "fglmc": li_b[i]["DataObj"][0]["FGLMC"],
                "fyxsxname": li_b[i]["DataObj"][0]["FYXSXNAME"],
                "fyxsx": li_b[i]["DataObj"][0]["FYXSX"],
                "fhscb": li_b[i]["DataObj"][0]["FHSCB"],
                "fbhscb": li_b[i]["DataObj"][0]["FBHSCB"],
                "fpricescale": str(int(li_b[i]["DataObj"][0]["FPRICESCALE"])),
                "flastprice": li_b[i]["DataObj"][0]["FLASTPRICE"],
                "fcansendqty": round(li_b[i]["DataObj"][0]["FCANSENDQTY"],1),
                "fnormallessqty": round(li_b[i]["DataObj"][0]["FCANSENDQTY"],1),
                "fypqty": round(li_b[i]["DataObj"][0]["FYPQTY"],1),
                "fcb": li_b[i]["DataObj"][0]["FCB"],
                "fqtyscale": int(li_b[i]["DataObj"][0]["FQTYSCALE"]),
                "fspxl": li_b[i]["DataObj"][0]["FSPXL"],
                "fspxlname": li_b[i]["DataObj"][0]["FSPXLNAME"],
                "funitold": int(li_b[i]["DataObj"][0]["FUNIT"]),
                "folongside": li_b[i]["DataObj"][0]["FOLONGSIDE"],
                "fovolume": '%e' % li_b[i]["DataObj"][0]["FOVOLUME"],
                "foweight": li_b[i]["DataObj"][0]["FOWEIGHT"],
                "is_hazardous_chemicals": int(li_b[i]["DataObj"][0]["IS_HAZARDOUS_CHEMICALS"]),
                "sublength": li_b[i]["DataObj"][0]["SUBLENGTH"],
                "minlength": li_b[i]["DataObj"][0]["MINLENGTH"],
                "fqty": float(num),
                "fqtybase": float(num),
                "fprice": li_b[i]["DataObj"][0]["FPRICE"],
                "fsysprice": li_b[i]["DataObj"][0]["FSYSPRICE"],
                'fdiscountrate': li_b[i]["DataObj"][0]["FLS"],
                'famt': num*li_b[i]["DataObj"][0]["FPRICE"],
                "distributor_price": li_b[i]["DataObj"][0]["FPRICE"],
                "distributor_amt": num*li_b[i]["DataObj"][0]["FPRICE"],
                'fzdamt': num*li_b[i]["DataObj"][0]["FPRICE"],
                'fzdjg': li_b[i]["DataObj"][0]["FPRICE"],
                'fentryid': i+1,    # 商品个数
                'fischeck': 1, 'fparentid': 0, 'saleentry_id': 0, 'distributor_discount': 1.0, 'ftakeprofile': 1, 'fisjy': '',
                'fhy': '', 'fsm': '', 'frlje': 0.0, 'fisjyname': '', 'frebfit': 0, 'frebfitname': '', 'fpfprice': 1.98,
                'fzxprice': 1.73, 'fsrcbilltype': '', 'flastyprice': 0.0, 'fsrcbillid': '', 'fscrbillfid': 0,
                'fscrbillfentryid': 0, 'ftpyprice': 1.485, 'fkjgz': '', 'ftpqty': 0.0, 'fbillprice': 0.0, 'fydkc': 0.0,
                'fdqty': 0.0, 'fdprice': 0.0, 'fdamt': 0.0, 'fuserjlrid': 0, 'fuserjlrname': '', 'fsourcedprice': 0.0,
                'fyigcgoid': 0, 'fyigocgsid': 0, 'fyigocgusefqty': 0.0, 'fzhdsl': '0', 'product_type': '0',
                'scrsaleentry_id': 0, 'unsubscribe_number': 0, 'refuse_number': 0, 'return_number': 0, 'purchaser': 0,
                'purchasername': '', 'categoryid': 0
            }
            li.append(ware)
            price_li.append(num*li_b[i]["DataObj"][0]["FPRICE"])
        total = 0
        for i in price_li:
            total += i
        data["distributor_amt"] = total
        data["bill_amt"] = total
        data["SaleEntries"] = li

        # 输入客户代码，传回参数
        url_cus = 'http://192.168.0.121:8012/Complex/Get_Organization'
        data_cus = {'number':cus_e.get(),
                'groupId':'85',
                'companyId':'257938',
                'isStock':False}
        res_cus = json.loads(requests.post(url_cus, data=data_cus).text)
        data["femployee"] = int(res_cus[0]['FEMPLOYEE'])
        data["fempname"] = res_cus[0]['FEMPNAME']
        data["faffiliatlinkman"] = res_cus[0]['FAFFILIATLINKMAN']
        data["fkfpyj"] = int(res_cus[0]['FKFPYJ'])
        data["fkfpyjname"] = res_cus[0]['FKFPYJNAME']
        data["finfor"] = res_cus[0]['FINFOR']
        data["fxsgsid"] = int(res_cus[0]['FXSGSID'])
        data["fxsgsname"] = res_cus[0]['FXSGSNAME']
        data["fpricetype"] = int(res_cus[0]['FPRICETYPE'])
        data["fpricetypename"] = res_cus[0]['FPRICETYPENAME']
        data["agencysales"] = int(res_cus[0]['AGENCYSALES'])
        data["agencysalesname"] = res_cus[0]['AGENCYSALESNAME']
        data["proxysale_companyid"] = res_cus[0]['PROXYSALE_COMPANYID']
        data["PROXYSALE_COMPANYNAME"] = res_cus[0]['PROXYSALE_COMPANYNAME']
        data["is_distributor"] = int(res_cus[0]['IS_DISTRIBUTOR'])
        data["distributor_discount"] = int(res_cus[0]['DISTRIBUTOR_DISCOUNT'])
        data["fsoncompanynumber"] = res_cus[0]['SONCOMPANY_ID']
        data["fsoncompanynumber"] = res_cus[0]['DEF_SALE_DEPT']
        # 获取发票单位代码
        url_unit = 'http://192.168.0.121:8012/Complex/Get_Customer'
        data_unit = {'content':cus_e.get()}
        res_unit = json.loads(requests.post(url_unit, data = data_unit).text)
        print(res_unit)
        data['fcustomerid'] = int(res_unit[0]['FITEMID'])
        if cus_e.get()=='05.02.0013':
            data['invoiceunit'] = 1
        data['invoiceunit'] = int(res_unit[0]['FITEMID'])
        res = requests.post(url, headers = header, data = json.dumps(data)).text
        print(res)
        record_e.delete(0,len(record_e.get()))
        record_e.insert(0,json.loads(res)['Data'])
        with open('记录单号.txt', 'a') as f:
            f.write(json.loads(res)['Data'] + '\t' +datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +'\n')
    except Exception as e:
        s = sys.exc_info()
        showerror('错误', message = str(e) + '\n' + '错误行数：'+ str(s[2].tb_lineno))

# 获取商品代码、仓库以及商品信息
def get_data(stockCode,btn):
    global lal_li
    global li_a
    global li_b
    li_a = []
    li_b = []
    with open('商品代码.txt', 'r') as f:
        c = f.readlines()
    for code in c:
        code = code.replace('\n','')
        url = 'http://192.168.0.121:8012/Complex/MerchandiseVerify_New'
        header = {'Content-Type': 'application/json'}
        data = {"content": code, "companyId": stockCode}
        res1 = requests.post(url, headers=header, data=json.dumps(data)).text
        a = str(int(json.loads(res1)[0]['FITEMID']))

        url = 'http://192.168.0.121:8012/Complex/Get_PriceStock'
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        data = {'soncompanyID': stockCode, 'customerID': '6144', 'priceTye': '918', 'ids': a}
        res2 = requests.post(url, headers=header, data=data).text
        li_a.append(json.loads(res1)[0])
        li_b.append(json.loads(res2))

    # 获取地理
    if btn.widgetName == 'address':
        address = province_e.get() + city_e.get() + district_e.get() + area_e.get()
        print(address)
        url = "http://api.map.baidu.com/geocoder?address=" + address + "&output=json&key=X2xwG17XDfD7Bv1Ujip2riCQNUR30eLH"
        res = requests.get(url).text
        res = json.loads(res)
        LAL.delete(0,len(LAL.get()))
        LAL.insert(0,str(res['result']['location']['lng'])+','+str(res['result']['location']['lat']))
        makeOrder(res["result"]["location"]["lng"], res["result"]["location"]['lat'], li_a, li_b, int(num_e.get()), date_e.get(), time_e.get(), stockCode)
    else:
        lal = LAL.get()
        lal_li = lal.split(',')
        url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=MmeyQy8TSMvXCuksAc0mMSN9cZRqdGGt&output=json&coordtype=bd09ll&location={},{}'.format(lal_li[1],lal_li[0])
        res = json.loads(requests.get(url).text)
        province_e.delete(0,len(province_e.get()))
        province_e.insert(0,res['result']['addressComponent']['province'])
        city_e.delete(0, len(city_e.get()))
        city_e.insert(0, res['result']['addressComponent']['city'])
        district_e.delete(0, len(district_e.get()))
        district_e.insert(0, res['result']['addressComponent']['district'])
        area_e.delete(0, len(area_e.get()))
        if res['result']['addressComponent']['town']=='' and res['result']['addressComponent']['town_code'] == '' and res['result']['addressComponent']['street'] == '' and res['result']['addressComponent']['street_number'] == '':
            area_e.insert(0,'')
        else:
            area_e.insert(0, res['result']['addressComponent']['town']+res['result']['addressComponent']['town_code']+res['result']['addressComponent']['street']+res['result']['addressComponent']['street_number'])
        # makeOrder(lal_li[0], lal_li[1], li_a, li_b, int(num_e.get()), date_e.get(), time_e.get(), stockCode)

# 根据经纬度制作订单
def lal_make():
    if stock.get() == '京南物流中心':
        t = threading.Thread(target=makeOrder, args=(lal_li[0], lal_li[1], li_a, li_b, int(num_e.get()), date_e.get(), time_e.get(), '257938'))
        t.start()
    else:
        t = threading.Thread(target=makeOrder, args=(lal_li[0], lal_li[1], li_a, li_b, int(num_e.get()), date_e.get(), time_e.get(), '756699'))
        t.start()

# 审核订单
def check(orderNum):
    # 查询订单金额
    url1 = 'http://192.168.0.121:8012/Sales/Get_Sale'
    data1 = {'id':record_e.get().replace('XS','')}
    res1 = json.loads(requests.post(url1, data = data1).text)
    total = res1['DataObj'][0]['BILL_AMT']
    try:
        url = 'http://192.168.0.121:8012/Sales/Check_Sale'
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        # with open('审核销售订单参数.txt',encoding='utf-8') as f:
        #     data = json.loads(f.read())
        current = int(time.time()*1000)
        data = {"Check_InvP_Amt":{"Check_InvP_Amt_Id":0,"XJ":total,"ZP":0.0,"SK":0.0,"JSH":"","Create_Time":None,"XJDS":0.0,"ZPDS":0.0,"YSAmt":0.0,"GRZZDS":0.0,"YConLineAmt":0.0,"YCACCountAmt":0.0,"Receivable_Dep_Id":0,"Is_ComPay":0,"Collection_Type":1,"Actual_Collection_Type":-1,"Invoice_Type":-1,"OtherBill_Date":"\/Date("+str(current)+"+0800)\/","Need_BringData":"","YSAmt_Checked":0,"XJ_Checked":1,"ZP_Checked":0,"SK_Checked":0,"YConLineAmt_Checked":0,"YCACCountAmt_Checked":0,"Check_Type":0,"Cash_Bank":11,"EnterpriseTransfers_Bank":126,"NetworkPayment_Bank":126,"Voucher_Bank":126,"BankAcceptance_Bank":126,"CommercialAcceptance_Bank":126,"Bill_Checked":0,"Voucher_Checked":0,"Voucher_Amt":0.0,"Voucher_Little":0.0,"BankAcceptance_Checked":0,"BankAcceptance":0.0,"BankAcceptance_Little":0.0,"CommercialAcceptance_Checked":0,"CommercialAcceptance":0.0,"CommercialAcceptance_Little":0.0,"CashBankList":None,"EnterpriseTransfersBankList":None,"NetworkPaymentBankList":None,"VoucherCheckBankList":None,"BankAcceptanceBankList":None,"CommercialAcceptanceBankList":None,"ReceivableCompanyType":2,"ReceivablesCompany":116488,"ReceivableCompanyChecked":0},"Checkinv_Log":{"FClass":0,"NewClass":0,"NewClass_Time":"\/Date("+str(current)+"+0800)\/","Customer_Id":0,"Amt":0.0,"Receivable_No":"","ReceivableRefund_No":"","OtherPayable_No":"","Receivable_Dep_Id":0,"Is_ComPay":0,"FInvoiceType":0,"AdvanceDate":"\/Date("+str(current)+"+0800)\/","FTakeNote":"","Status":0,"Cash_Bank":11,"EnterpriseTransfers_Bank":126,"NetworkPayment_Bank":126,"Voucher_Bank":126,"BankAcceptance_Bank":126,"CommercialAcceptance_Bank":126,"Bill_Checked":0,"Voucher_Checked":0,"Voucher_Amt":0.0,"Voucher_Little":0.0,"BankAcceptance_Checked":0,"BankAcceptance":0.0,"BankAcceptance_Little":0.0,"CommercialAcceptance_Checked":0,"CommercialAcceptance":0.0,"CommercialAcceptance_Little":0.0,"CashBankList":None,"EnterpriseTransfersBankList":None,"NetworkPaymentBankList":None,"VoucherCheckBankList":None,"BankAcceptanceBankList":None,"CommercialAcceptanceBankList":None},"Sales":[{"FId":25895422,"FbillId":"XS25895422","FCheckId":21724,"CheckName":"陈化淳","Receivable_dep_Id":382853,"CollectionType":1,"CollectionType_Back":0,"FDEPTId":419509,"Staff_SignaTure_Id":0,"Receivables_no":None,"Advance_no":None,"Com_Receivables_no":None,"Com_Advance_no":None,"Com_Payable_no":None,"UnReceivables_no":None,"Seal_UserId":0,"AccountReceivable_UserId":0,"Bill_Amt":total,"Actual_Collection_Type":-1,"Is_Use_XZL":0}],"CashWarrant":True}
        data["Sales"][0]["FId"] = orderNum.replace('XS','')
        data["Sales"][0]["FbillId"] = orderNum
        res = requests.post(url, headers = header, data = json.dumps(data)).text
        if '"Data":"[{}]"'.format(record_e.get().replace('XS','')) in res:
            showinfo('成功！','审核成功！')
            print(res)
        else:
            raise Exception(res)
    except Exception as e:
        showerror('错误',e)

# 盖章
def gaizhang(num):
    try:
        url = 'http://192.168.0.121:8012/Sales/Check_SaleStamp'
        # url = 'http://111.200.196.1:8012/Sales/Check_SaleStamp'
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        data = [{"Fid":"int(num.replace('XS',''))","FBillId":num,"Receivables_no":"","Advance_no":"","Com_Receivables_no":"","Com_Advance_no":"","Com_Payable_no":"","UnReceivables_no":"","Seal_UserId":21724}]
        res = requests.post(url, headers = header, data = json.dumps(data)).text
        if '"Message":"盖章成功"' in res:
            showinfo('成功！', '盖章成功！')
            print(res)
        else:
            raise Exception(res)
    except Exception as e:
        showerror('错误',e)

# 点击制作
def th_make(btn):
    config.set('address','province',province_e.get())
    config.set('address', 'city', city_e.get())
    config.set('address', 'district', district_e.get())
    config.set('address', 'area', area_e.get())
    config.set('address', 'number', num_e.get())
    config.set('address', 'code', cus_e.get())
    config.write(open('config.ini', 'w'))

    if stock.get() == '京南物流中心':
        t = threading.Thread(target=get_data, args=('257938',btn))
        t.start()
    else:
        t = threading.Thread(target=get_data, args=('756699',btn))
        t.start()

# 点击审核
def th_check():
    t = threading.Thread(target=check, args=(record_e.get(),))
    t.start()

#点击盖章
def th_gaizhang():
    t = threading.Thread(target=gaizhang, args=(record_e.get(),))
    t.start()

# 加载配置
if os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config.read('config.ini')
    pro = config.get('address','province')
    ci = config.get('address', 'city')
    dis = config.get('address', 'district')
    ar = config.get('address', 'area')
    nu = config.get('address', 'number')
    code = config.get('address', 'code')
else:
    config = configparser.ConfigParser()
    config.add_section('address')
    pro = ''
    ci = ''
    dis = ''
    ar = ''
    nu = ''
    code = ''

gui = tk.Tk()
gui.geometry('550x280+580+300')
# 订单类型
orderType = ttk.Combobox(gui, textvariable = tk.StringVar())
orderType['value'] = ('物流配送', '店面配送')
orderType.current(0)
orderType.place(rely = 0.05, relx = 0.03, width = 80)
# 地址
tk.Label(gui, text = '省', font = 10).place(rely = 0.13, relx = 0.03)
province_e = tk.Entry(gui, font = 8)
province_e.insert(0,pro)
province_e.place(rely = 0.13, relx = 0.07,width = 80)
tk.Label(gui, text = '市', font = 10).place(rely = 0.13, relx = 0.2)
city_e = tk.Entry(gui, font = 8)
city_e.insert(0,ci)
city_e.place(rely = 0.13, relx = 0.24,width = 80)
tk.Label(gui, text = '区', font = 10).place(rely = 0.13, relx = 0.37)
district_e = tk.Entry(gui, font = 8)
district_e.insert(0,dis)
district_e.place(rely = 0.13, relx = 0.41,width = 80)
tk.Label(gui, text = '详细地址', font = 10).place(rely = 0.13, relx = 0.54)
area_e = tk.Entry(gui, font = 8)
area_e.insert(0,ar)
area_e.place(rely = 0.13, relx = 0.67,width = 120)
# 仓库
stock = ttk.Combobox(gui, textvariable = tk.StringVar())
stock['value'] = ('京南物流中心', '京北物流中心')
stock.current(0)
stock.place(rely = 0.25, relx = 0.03, width = 100)
# 数量
tk.Label(gui, text = '商品数量', font = 10).place(rely = 0.25, relx = 0.23)
num_e = tk.Entry(gui, font = 8)
num_e.insert(0,nu)
num_e.place(rely = 0.25, relx = 0.359, width = 50)
# 送货时间
tk.Label(gui, text = '送货时间', font = 10).place(rely = 0.25, relx = 0.46)
date_e = ttk.Combobox(gui, textvariable = tk.StringVar())
date_e['value'] = ('明天','后天','大后天')
date_e.current(0)
date_e.place(rely = 0.25, relx = 0.59, width = 60)
time_e = ttk.Combobox(gui, textvariable = tk.StringVar())
time_e['value'] = ('白天送', '上午送', '下午送', '夜间送')
time_e.current(0)
time_e.place(rely = 0.25, relx = 0.73, width = 80)
# 制作订单
make_btn = tk.Button(gui, text = '制作订单', font = 8, command = lambda:th_make(make_btn))
make_btn.widgetName = 'address'
make_btn.place(rely = 0.37, relx = 0.15)
check_btn = tk.Button(gui, text = '审核订单', font = 8, command = th_check)
check_btn.place(rely = 0.37, relx = 0.35)
stamp_btn = tk.Button(gui, text = '盖章订单', font = 8, command = th_gaizhang)
stamp_btn.place(rely = 0.37, relx = 0.55)
# 生成的单号
record_e = tk.Entry(gui, font = 5)
record_e.place(rely = 0.49, relx = 0.35, width = 100)
# 经纬度
tk.Label(gui, text = '经纬度:', font = 10).place(rely = 0.61, relx = 0.03)
LAL = tk.Entry(gui, font = 5)
LAL.place(rely = 0.61, relx = 0.15, width = 300)
# 根据经纬度制作
LAL_btn = tk.Button(gui, text = '获取定位',font = 8, command = lambda:th_make(LAL_btn))
LAL_btn.widgetName = 'LAL'
LAL_btn.place(rely = 0.73, relx = 0.15)
LAL1_btn = tk.Button(gui, text = '制作',font = 8, command = lal_make)
LAL1_btn.place(rely = 0.73, relx = 0.35)
# 输入客户代码
tk.Label(gui, text = '客户代码:', font = 10).place(rely = 0.49, relx = 0.001)
cus_e = tk.Entry(gui, font = 5)
cus_e.insert(0,code)
cus_e.place(rely = 0.49, relx = 0.15,width = 90)
# 允许拣货
def allowpick():
    if record_e.get() == '':
        showerror('错误','先填写单据号！')
    else:
        # 获取销售单ID
        url = 'https://t4.fsyuncai.com/tmspc/saleOrder/saleOrderList'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/json',
                  'Cookie': 'm_tk=0f3cOT1XkgMBqLCp7SVNw71od3b7VxnNu8pBekdv+WB6rMr8a2ZQoXGuIp%2FN3TyCQbxP0lLeRx7MyBfwego0hRnZ3V2W45JZGCljkRmFjQPqEO+3ClTcaQDb76J46Cynnp24KYLlXrckUbpxYNas9g; token=c9690e3edc7e682f2e4261dc4049e8d4'}
        data = {"pageNum":1,"pageSize":10,"sortObject":{"sortKey":0,"sortValue":0},"deliveryMethod":"1","companyId":257938,"authQuery":"","latestDeliveryTime":None,"saleBillNo":None,"dispatcherBillNo":None,"inCompanyId":None,"billIds":None,"provinceId":"","cityId":"","areaId":"","advancedQueryList":[{"concatSymbol":"and","bracketLeft":"","controlType":"10","frontName":"运单号","compareSymbol":"=","bracketRight":"","controlHasCandidate":0,"value":record_e.get(),"dataType":"10","controlCandidateValue":"","dbName":"s.sale_bill_no","sequence":0,"showType":0}],"isUrgent":0,"isLimit":0,"isLack":0,"isIncludeSpecial":0,"isRefund":0,"isIncludeMutex":0,"wareHouseId":None,"isChangeCompany":0,"isInclude9999":2,"differenceSplitOrder":0,"routeKey":None,"weightLoad":None,"volumeLoad":None,"saleBillId":None,"distance":None,"billStatus":1}
        res = json.loads(requests.post(url , headers = header, data = json.dumps(data)).text)
        try:
            id = res['data']['data'][0]['saleBillId']
            print(id)
        except:
            showerror('失败','单据还没推到T')
        else:
            # 调用允许拣货
            url = 'https://t4.fsyuncai.com/tmspc/saleOrder/pickingAllow'
            data = {"confirmPush":2,"id":0,"orderBillIdList":[id]}
            res = requests.post(url, headers = header, data = json.dumps(data)).text
            data = {"confirmPush":1,"id":0,"orderBillIdList":[id]}
            res = requests.post(url, headers = header, data = json.dumps(data)).text
            print(res)
            if '操作成功' in res:
                showinfo('操作成功', '允许拣货！')

            else:
                showerror('操作失败','允许拣货失败!')

allowpick_btn = tk.Button(gui, text = '允许拣货', font = 8, command = lambda:threading.Thread(target=allowpick).start())
allowpick_btn.place(rely = 0.37, relx = 0.75)

gui.mainloop()