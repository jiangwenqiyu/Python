import requests
import json
import time
import getSign
import base64
import pymysql
import threading
import pymysql
import datetime

# 公用参数
class basicInfo(object):
    token = ''
    public_parameter = {
        'loginAccount':'',
        'memberId':'',
        'customerId':'',
        'customerCode':'',
        'provinceId':'',
        'provinceCode':'',
        'cityId':'',
        'cityCode':'',
        'districtId':'',
        'districtCode':'',
        'streetId':'',
        'streetCode':'',
        'token':'',
        'skuCode':'',
        'warehouse':'',
        'privince':'',
        'city':'',
        'district':'',
        'street':'',
        'sku':'',
        'orderid':'',
        'payMoney':'',
        'limitLine':'',
        'lng':'',
        'lat':''
    }
    def __init__(self):
        self.host = 'https://t2.fsyuncai.com'

# 获取 四级地址
class getAddress(basicInfo):
    def __init__(self, first, second, third, forth):
        self.first = first
        self.second = second
        self.third = third
        self.forth = forth
        self.public_parameter['province'] = first
        self.public_parameter['city'] = second
        self.public_parameter['district'] = third
        self.public_parameter['street'] = forth
        self.address = first + second + third + forth
        self.getAddrCode()

    def getAddrCode(self):
        connect = pymysql.connect(host = '192.168.0.27', user = 'developer', password = 'dev_123', database = 'xfs_common', use_unicode =True, charset = 'utf8')
        cur = connect.cursor()
        word = "select address_id, code, name from address_library where level={} and name='{}' and parent_code=''".format(101, self.first)
        cur.execute(word)
        data1 = cur.fetchall()
        self.public_parameter['provinceId'] = data1[0][0]
        self.public_parameter['provinceCode'] = data1[0][1]

        word = "select address_id, code, name from address_library where level={} and name='{}' and parent_code={}".format(102, self.second, data1[0][1])
        cur.execute(word)
        data2 = cur.fetchall()
        self.public_parameter['cityId'] = data2[0][0]
        self.public_parameter['cityCode'] = data2[0][1]

        word = "select address_id, code, name from address_library where level={} and name='{}' and parent_code={}".format(103, self.third, data2[0][1])
        cur.execute(word)
        data3 = cur.fetchall()
        self.public_parameter['districtId'] = data3[0][0]
        self.public_parameter['districtCode'] = data3[0][1]

        word = "select address_id, code, name, limit_line from address_library where level={} and name='{}'".format(104, self.forth)
        cur.execute(word)
        data4 = cur.fetchall()
        self.public_parameter['streetId'] = data4[0][0]
        self.public_parameter['streetCode'] = data4[0][1]
        self.public_parameter['limitLine'] = data4[0][2]

        # 获取经纬度
        url = "http://api.map.baidu.com/geocoder?address=" + self.address + "&output=json&key=X2xwG17XDfD7Bv1Ujip2riCQNUR30eLH"
        res = json.loads(requests.get(url).text)
        self.public_parameter['lng'] = res['result']['location']['lng']
        self.public_parameter['lat'] = res['result']['location']['lat']

        cur.close()
        connect.close()

# 创建session对象
class createSession(basicInfo):
    def __init__(self):
        self.session = requests.session()
        super().__init__()

# 登录
class Login(createSession):
    '''登录'''
    def log(self, user, pwd, typee):
        self.public_parameter['type'] = typee
        self.public_parameter['loginAccount'] = user
        code, uuid = self.getCode()
        pwd = base64.b64encode(pwd.encode()).decode()
        url = '{}/api/pc/membership/loginServiceV1'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01'}
        data = {'loginAccount':user,
                'password':pwd,
                'uuid':uuid,
                'code':code,
                'platform':'pc',
                'member_id':'',
                'account_type':'',
                'token':'',
                'timestamp':int(time.time() * 1000),
                'device_platform':'pc',
                'customer_id':'',
                'customer_code':'',
                'sign':'45b975e55d73dcb52dda3a5047930439'}
        sign = getSign.generateSign(data)
        data['sign'] = sign
        res = json.loads(self.session.post(url, headers = header, data = data).text)

        # 返回相关客户信息
        if self.public_parameter['type'] == '签约客户':
            memberId = res['memberInfo']['memberId']
            customerId = res['crmCustomerInfos'][0]['customerId']
            customer_code = res['crmCustomerInfos'][0]['customerCode']
            self.public_parameter['memberId'] = memberId
            self.public_parameter['customerId'] = customerId
            self.public_parameter['customerCode'] = customer_code
            self.public_parameter['token'] = res['token']
        elif self.public_parameter['type'] == '普通客户':
            memberId = res['memberInfo']['memberId']
            customerId = ''
            customer_code = ''
            self.public_parameter['memberId'] = memberId
            self.public_parameter['customerId'] = customerId
            self.public_parameter['customerCode'] = customer_code
            self.public_parameter['token'] = res['token']

    # 获取uuid、验证码
    def getCode(self):
        url = '{}/api/pc/membership/getImgVerifyCode.jhtml'.format(self.host)
        header = {'Accept': '*/*',
                  'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'uuidParam':'',
                'member_id':'',
                'account_type':'',
                'token':'',
                'timestamp': int(time.time() * 1000),
                'device_platform': 'pc',
                'customer_id':'',
                'customer_code':'',
                'sign': '6f9cea932652222cff7e32659245aaac'}
        sign = getSign.generateSign(data)
        data['sign'] = sign
        res = json.loads(self.session.post(url, headers= header, data = data).text)
        code = res['code']
        uuid = res['uuid']
        return code, uuid

# 获取提交订单所需参数
class getSubmitOrderCanshu(Login):
    # 根据城市code，获取的仓库id
    def getStockCode(self):
        url = '{}/api/pc/baseservice/area/getAddressDataByCode'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01'}
        data = {'code':self.public_parameter['cityCode'],   # 市code  110100
                'member_id':self.public_parameter['memberId'],
                'account_type':'10',
                'token':self.public_parameter['token'],
                'timestamp':int(time.time() * 1000),
                'device_platform':'pc',
                'customer_id':self.public_parameter['customerId'],
                'customer_code':self.public_parameter['customerCode'],
                'sign':'07a1f23ff1c25ccd64708fb15c128390'}
        data['sign'] = getSign.generateSign(data)
        res = json.loads(self.session.post(url, headers = header, data = data).text)
        warehouse_code = res['data']['warehouse_code']
        self.public_parameter['warehouse'] = warehouse_code
        return warehouse_code

    # 拿到购物车里所有商品信息，组成列表，返回
    def getPrice(self):
        url = '{}/api/pc/cart/getShoppingCartList'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type':'application/json'}
        data = {
            "memberId": self.public_parameter['memberId'],
            "cityId": self.public_parameter['cityCode'],
            "customerId": self.public_parameter['customerId'],
            "token": self.public_parameter['token'],
            "warehouseId": self.public_parameter['warehouse'],
            "platformType": 1,
            "accountType": "10",
            "loginAccount": self.public_parameter['loginAccount'],
            "isMiniOrderStatus": 20,
            "curSiteCode": self.public_parameter['provinceCode'],   # 省级编码
            "mainCustomerId": "359",   # 客户组id
            "member_id": self.public_parameter['memberId'],
            "account_type": "10",
            "timestamp": int(time.time() * 1000),
            "device_platform": "pc",
            "customer_id": self.public_parameter['customerId'],
            "customer_code": self.public_parameter['customerCode'],
            "sign": "a4c364849582f0249c52d8482d1cf7a7"
        }
        data['sign'] = getSign.generateSign(data)
        res = json.loads(self.session.post(url, headers = header, data = json.dumps(data)).text)
        shopCarWare = list()
        for waresDict in res['promotionProducts']:
            wareInfo = dict()
            wareInfo['skuCode'] = waresDict['shoppingCartList'][0][0]['sku_code']
            wareInfo['salePrice'] = waresDict['shoppingCartList'][0][0]['salePrice']
            wareInfo['promotionPrice'] = 0                 # 促销优惠金额
            wareInfo['activityId'] = 0                     # 促销活动ID
            wareInfo['buyyerCount'] = waresDict['shoppingCartList'][0][0]['productCount']    # 购买数量
            wareInfo['cartId'] = waresDict['shoppingCartList'][0][0]['id']   # 购物车ID
            wareInfo['joinPromotionTag'] = '10'    # 参与促销标记：10-参与；20-不参与（新增字段，默认传：10）
            wareInfo['tempPurchase'] = '20'        # 临采商品: 10 - 是；20 - 否
            shopCarWare.append(wareInfo)
        return shopCarWare

    # 提交订单的其他参数信息
    def otherInfo(self, transport):
        if transport == '鑫方盛物流':
            transway = 'privateFreight'
        elif transport == '第三方物流':
            transway = ''
        elif transport == '上门自提':
            pass

        temp_skuList = self.getPrice()
        skuList = list()
        for i in temp_skuList:
            i.pop('promotionPrice')
            i.pop('tempPurchase')
            skuList.append(i)

        url = '{}/api/pc/trade/settleOrder'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/json'}
        data = {
            "skuList": skuList,
            "cityId": self.public_parameter['cityCode'],
            "warehouseId": self.getStockCode(),
            "userChangeDeliver": "",
            "member_id": self.public_parameter['memberId'],
            "account_type": "10",
            "token": self.public_parameter['token'],
            "timestamp": int(time.time() * 1000),
            "device_platform": "pc",
            "customer_id": self.public_parameter['customerId'],
            "customer_code": self.public_parameter['customerCode'],
            "sign": "9071fa6ecde5edde550dd1abf589c17f"
        }

        data['sign'] = getSign.generateSign(data)
        res = json.loads(self.session.post(url, headers = header, data = json.dumps(data)).text)
        finalTotalAmount = res['payTotalMoney']
        goodTotalMoney = res['goodTotalMoney']
        goodTotalNum = res['skuTotalNum']
        goodTotalWeight = res['goodTotalWeight']
        # print(res)
        yunfei = res['freight'][transway]
        # ship_add_id = res['shippingAddressModel']['ship_add_id']
        return finalTotalAmount, goodTotalMoney, goodTotalNum, goodTotalWeight, yunfei

# 加购，提交订单
class wareOperator(getSubmitOrderCanshu):
    '''操作商品'''
    # 加购物车
    def addShoppingCar(self, skuDict):
        skuList = list()
        for sku in skuDict:
            tempDict = dict()
            tempDict['skuId'] = ''
            tempDict['skuCode'] = sku
            tempDict['skuNum'] = skuDict[sku]
            skuList.append(tempDict)

        url = '{}/api/pc/cart/addShoppingCartReturnSku'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/json'}
        data = {
            "memberId": self.public_parameter['memberId'],
            "token": self.public_parameter['token'],
            "customerId": self.public_parameter['customerId'],
            "cityId": self.public_parameter['cityCode'],
            "warehouseId": self.getStockCode(),
            "skuIdNumlist": skuList,
            "platformType": 1,
            "member_id": self.public_parameter['memberId'],
            "account_type": "10",
            "timestamp": int(time.time() * 1000),
            "device_platform": "pc",
            "customer_id": self.public_parameter['customerId'],
            "customer_code": self.public_parameter['customerCode'],
            "sign": "1573815209d74dfb613a26fc81e95928"
        }
        if self.public_parameter['type'] == '普通客户':
            data['account_type'] = 20
        sign = getSign.generateSign(data)
        data['sign'] = sign
        res = json.loads(self.session.post(url, headers = header, data = json.dumps(data)).text)
        self.public_parameter['sku'] = skuDict
        if res['errorMessage'] == '加入购物车成功':
            print('加购成功！')
        else:
            print(res)

    # 提交订单
    def submitOrder(self, paymod, transport, recvName, phone):
        finalTotalAmount, goodTotalMoney, goodTotalNum, goodTotalWeight, yunfei = self.otherInfo(transport)
        skuModelList = self.getPrice()

        goodTotalMoney = 0
        for i in skuModelList:
            goodTotalMoney += float(i['salePrice']) * float(i['buyyerCount'])
        finalTotalAmount = round(goodTotalMoney + yunfei, 2)

        url = '{}/api/pc/trade/submitOrder'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/json'}
        data = {
            "usedIntegral": 0,          # 使用积分数
            "qualityFileRequired": 20,  #  是否需要资质文件: 10-需要;20-不需求
            "couponCode": "",           # 优惠券编码
            "usedCoupon": "20",         # 20不用优惠券
            "skuModelList": skuModelList,
            "finalTotalAmount": 0,    # 总价格，含运费
            "goodTotalMoney": 0,      # 总价格，不含运费
            "goodTotalNum": 0,       # 商品总数
            "goodTotalWeight": 0,  # 总重量
            "payMoney": 0,            # 应付总额
            "payModel": {
                "id": "",
                "payName": "银行转账",
                "payType": paymod,
                "paySubType": ""
            },
            "address": {
                "id": "",
                "ship_add_id": 147,    # 地址ID
                "province_id": self.public_parameter['provinceId'],
                "province_code": self.public_parameter['provinceCode'],
                "provinceName": self.public_parameter['province'],
                "city_id": self.public_parameter['cityId'],
                "city_code": self.public_parameter['cityCode'],
                "cityName": self.public_parameter['city'],
                "district_id": self.public_parameter['districtId'],
                "district_code": self.public_parameter['districtCode'],
                "areaName": self.public_parameter['district'],
                "street_id": self.public_parameter['streetId'],
                "street_code": self.public_parameter['streetCode'],
                "streetName": self.public_parameter['street'],
                "detail_address": "是",
                "add_alias": "",       # 地址别名/自提点名称
                "address_type": "",    # 地址类型：10=分销地址
                "office_phone": "",
                "email": "",
                "is_default": "1",
                "parent_warehouse_code": self.public_parameter['warehouse'],    # 父仓库编码
                "warehouse_code": self.public_parameter['warehouse'],           # 子仓库编码
                "limitLine": self.public_parameter['limitLine'],               # 是否限行：10-限行；20-不限行
                "addressPersonList": [{
                    "id": "",
                    "addressId": 105,
                    "receiverName": recvName,
                    "mobile": phone,
                    "status": "10"
                }],
                "address_source": "10",       # 地址来源：10-收货地址；20-自提地址
                "lng": self.public_parameter['lng'],
                "lat": self.public_parameter['lat'],
                "longitude": None,
                "latitude": None,
                "temp_address": None,
                "distance": None,
                "isLastAddress": None
            },
            "limitLine": self.public_parameter['limitLine'],               # 是否限行：10-限行；20-不限行
            "deliverWay": "private",         # 选中的物流方式：private-自有物流;kd-快递;ky-快运;car-专车包车;zt-自提
            "wannaArrivedTimeBy": 10,
            "wannaArrivedAtBegin": (datetime.datetime.now() + datetime.timedelta(days=5)).strftime('%Y-%m-%d') + " 12:00:00",
            "wannaArrivedAtEnd": (datetime.datetime.now() + datetime.timedelta(days=5)).strftime('%Y-%m-%d') + " 17:00:00",
            "freight": '',                   # 运费
            "separateShippingFee": 10,        # 是否单开运费: 10-是；20-否
            "invoiceFlag": 10,                # 是否选择开发票：10-不开发票；20-开发票
            "member_id": self.public_parameter['memberId'],
            "account_type": "10",
            "token": self.token,
            "timestamp": int(time.time() * 1000),
            "device_platform": "pc",
            "customer_id": self.public_parameter['customerId'],
            "customer_code": self.public_parameter['customerCode'],
            "sign": "a88d216b5a565c83827b9d88d4027d8c"
        }
        if self.public_parameter['type'] == '普通客户':
            data['account_type'] = 20
        data['sign'] = getSign.generateSign(data)
        res = json.loads(self.session.post(url, headers = header, data = json.dumps(data)).text)
        self.public_parameter['orderid'] = res['orderId']
        self.public_parameter['payMoney'] = finalTotalAmount
        if res['msg'] == 'SUCCESS':
            print('单号：', res['orderId'])
        else:
            print(res)

# 确认付款提交
class confirmPay(Login):
    # 银行转账, 直接确认
    def confirmYinhang(self):
        url = '{}/api/pc/order/payment/instantConfirm'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'X-Requested-With': 'XMLHttpRequest',
                  'Origin': 'https://t2.fsyuncai.com',
                  'Sec-Fetch-Dest': 'empty',
                  'Content-Type': 'application/json'}
        data = {
            "order_id": self.public_parameter['orderid'],
            "member_id": self.public_parameter['memberId'],
            "current_type": 1,
            "paid_id": self.public_parameter['orderid'],
            "login_account": self.public_parameter['loginAccount'],
            "account_type": "10",
            "token": self.public_parameter['token'],
            "timestamp": int(time.time() * 1000),
            "device_platform": "pc",
            "customer_id": self.public_parameter['customerId'],
            "customer_code": self.public_parameter['customerCode'],
            "sign": "548eed820bd8170552ba8f61162199c6"}

        sign = getSign.generateSign(data)
        data['sign'] = sign
        res = self.session.post(url, headers = header, data = json.dumps(data)).text
        print(res)

    # 账期支付的参数获取
    def parameterZhangqi(self):
        url = '{}/api/pc/payment/save_pay_info'.format(self.host)
        header = {'Accept': '*/*',
                  'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'orderIds':self.public_parameter['orderid'],
                'memberId':self.public_parameter['memberId'],
                'payType':'10',
                'payWayCode':'1201',
                'totalAmount':self.public_parameter['payMoney'],
                'customerId':self.public_parameter['customerId'],
                'customerCode':self.public_parameter['customerCode'],
                'member_id':self.public_parameter['memberId'],
                'account_type':'10',
                'token':self.public_parameter['token'],
                'timestamp':int(time.time() * 1000),
                'device_platform':'pc',
                'customer_id':self.public_parameter['customerId'],
                'customer_code':self.public_parameter['customerCode'],
                'sign':'699595713b4f6aa9b7d24d08da418de8'}
        data['sign'] = getSign.generateSign(data)
        res = json.loads(self.session.post(url, headers = header, data = data).text)
        return res['payInfo']['payId'], res['totalAmount']

    # 账期支付，需要先获取参数
    def confirmZhangqi(self, paypassword):
        payId, payableAmount = self.parameterZhangqi()
        paypassword = base64.b64encode(paypassword.encode()).decode()
        url = '{}/api/pc/payment/combine_pay'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/json'}
        data = {
            "params": [{
                "payId": payId,
                "payWayName": "AccountPayPC",
                "payableAmount": payableAmount,
                "platform": 10,
                "desc": "zhangqizhifu",
                "accountPwd": paypassword, # "MDAwMDAw"
            }],
            "member_id": self.public_parameter['memberId'],
            "account_type": "10",
            "token": self.public_parameter['token'],
            "timestamp": int(time.time() * 1000),
            "device_platform": "pc",
            "customer_id": self.public_parameter['customerId'],
            "customer_code": self.public_parameter['customerCode'],
            "sign": "4d0c68c3bbcff726a21fa9e0074d7347"
        }
        data['sign'] = getSign.generateSign(data)
        res = self.session.post(url, headers = header, data = json.dumps(data)).text
        print(payableAmount)
        print(res)

# 后台确认收款
class backConfirm(basicInfo):
    # 支付金额
    def getMoney(self):
        url = '{}/api/admin/aorder/confirm/getBankInfo'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        data = {'order_id':self.public_parameter['orderid']}
        res = json.loads(requests.post(url, headers = header, data = data).text)
        return res['data']['paidAmount']

    # 确认收款
    def makesure(self):
        money = float(self.getMoney())
        print(money)
        url = '{}/api/admin/aorder/confirm/comfirmMoney'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/json'}
        data = {'bus_id': self.public_parameter['orderid'],
                'operate_userid': 340,
                'operate_username': "姜彦辰",
                'due_account_name': "北京鑫方盛电子商务有限公司",
                'due_account_number': "100530969410010004",
                'due_bank_name': "邮政储蓄银行北京兴华路支行",
                'due_line_number': "4031 0000 3369",
                'due_amount': money,
                'due_account_id': "125",
                'due_company_code': "201",
                'actual_account_name': "北京鑫方盛电子商务有限公司",
                'actual_account_number': "100530969410010004",
                'actual_bank_name': "邮政储蓄银行北京兴华路支行",
                'actual_line_number': "4031 0000 3369",
                'actual_amount': "113.90",
                'remark': "123",
                'orderProofList': [],
                'actual_account_id': money,
                'actual_company_code': "201"}
        res = requests.post(url, headers = header, data = json.dumps(data)).text
        print(res)

def main():
    obj = getAddress('北京市', '北京市', '大兴区', '兴丰街道')
    Login().log('13681376038', 'jyc1995824', '普通客户')
    print('登录成功！  token为:', basicInfo.public_parameter['token'])

    # 操作商品对象
    wareopera = wareOperator()

    print('*****************加购*****************')
    wareDict = {'033174':99999}
    wareopera.addShoppingCar(wareDict)
    time.sleep(2)

    print('*****************提交*****************')
    wareopera.submitOrder('1301', '鑫方盛物流', '姜姜姜', '15210123567')   # 1301 银行转账    1201 账期      # 默认鑫方盛物流
    time.sleep(5)

    # print('确认')
    # confirmPay().confirmYinhang()
    # confirmPay().confirmZhangqi('950824')
    # time.sleep(3)
    #
    # print('后台收款')
    # backConfirm().makesure()


if __name__ == '__main__':
    main()


