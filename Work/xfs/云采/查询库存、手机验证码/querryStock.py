import requests
import json
import tkinter
import cx_Oracle

# 198代表小井分公司
def getStock(wareCode = '047706', companyID = 116488):
    # 先根据商品代码、公司id，获取itemID；然后利用itemID获取到对应公司、商品的库存
    url = 'http://111.200.196.1:8012/Complex/MerchandiseVerify_New'
    header = {'Content-Type': 'application/json'}
    data = {"content":wareCode,"companyId":companyID}
    res = json.loads(requests.post(url, headers = header, data = json.dumps(data), verify = False).text)

    url = 'http://111.200.196.1:8012/Complex/Get_PriceStock'
    header['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
    data = {'soncompanyID':companyID,   # 公司ID
            'customerID':6144,          # 客户ID，不用管
            'priceTye':918,             # 价格类型，不用管
            'ids':int(res[0]['FITEMID'])}         # 根据公司、商品返回的值
    res = json.loads(requests.post(url, headers = header, data = data).text)
    stock = res['DataObj'][0]['FCANSENDQTY']
    return stock

def getCompanyID(comnpanyName):
    connect = cx_Oracle.connect('SUPPLIER', 'SUPPLIER', '192.168.0.11:1521/XFS')
    cur = connect.cursor()
    word = "SELECT soncompany_id as 公司id,fwmscompanyid 库存中心id FROM t_company where fname='{}'".format(comnpanyName)
    cur.execute(word)
    data = cur.fetchall()
    if data[0][1] == 257938:
        companyID = 257938
    else:
        companyID = data[0][0]
    cur.close()
    connect.close()
    return int(companyID)

while True:
    wareCode = input('输入商品代码:')
    companyName = '小井分公司'
    companyID = getCompanyID(companyName)
    stock = getStock(wareCode = wareCode,companyID = companyID)
    logisticsStock = getStock(wareCode = wareCode,companyID = 257938)
    print('%s门店库存: %s' % (companyName,stock))
    print('京南物流中心库存: %s' % logisticsStock)

