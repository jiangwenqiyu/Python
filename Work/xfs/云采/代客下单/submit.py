import requests
import json
import threading

class basicInfo(object):
    def __init__(self):
        self.host = 'https://t2.fsyuncai.com'

# 获取客户信息
class CustomerInfo(basicInfo):
    # 获取客户代码、客户ID
    def getCustomerInfo(self, phone):
        url = '{}/membership/lenovoCustomerInfo.jhtml'.format(self.host)
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        data = {'customerName':'',
                'mobilePhone':phone,
                'loginAccount':'',
                'pageNum':'1',
                'pageSize':'100'}
        res = json.loads(requests.post(url, headers = header, data = data).text)
        customer_id = res['subAccountList'][0]['customer_id']
        consumer_code = res['subAccountList'][0]['consumer_code']
        return customer_id, consumer_code

    # 根据客户ID、手机号，得到会员id
    def getMemberId(self, customerId, phone):
        url = '{}/membership/queryLoginAccountForCustomerId.jhtml'.format(self.host)
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        data = {'customerId':customerId,
                'mobilePhone':phone,
                'loginAccount':''}
        res = json.loads(requests.post(url, headers = header, data = data).text)
        memberid = res['data'][0]['memberId']
        return memberid

# 获取地址、限行
class getAddress(CustomerInfo):
    def getAddr(self, add, parcode, typ):
        url = '{}/abaseservice/area/getLowerAddress'.format(self.host)
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        data = {'parentCode': parcode}
        res = json.loads(requests.post(url, headers = header, data = data).text)

        if typ == 2:
            t = list()
            for i in res['list']:
                t.append(i['name'])
            return t
        else:
            for i in range(len(res['list'])):
                if add == res['list'][i]['name']:
                    provincecode = res['list'][i]['code']
                    provinceid = res['list'][i]['address_id']
                    limit_line = res['list'][i]['limit_line']
                    return provincecode, provinceid, limit_line

# 获取商品信息
class getWare(getAddress):
    def getWareInfo(self, customerId, cityCode, memberId, districtCode, warehouse, skucode):
        url = '{}/aproduct/product/getValetOrderSearchForK3'.format(self.host)
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        data = {"productCodeOrName":skucode,
                "codeList":None,
                "customerId":customerId,
                "cityCode":cityCode,
                "searchType":"0",
                "categoryLevel":"",
                "memberId":memberId,
                "subWareHouseId":warehouse,
                "districtCode":districtCode}
        res = json.loads(requests.post(url, headers = header, data = json.dumps(data)).text)
        price = res['data'][0]['price']
        skuid = res['data'][0]['sku_id']
        number_decimal = res['data'][0]['number_decimal']
        return price, skuid, number_decimal

    # 获取对应仓
    def getStock(self, citycode, areacode):
        url = '{}/baseservice/area/getAddressCorrespondWarehouse'.format(self.host)
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        data = {'code':citycode,
                'areaCode':areacode}
        res = json.loads(requests.post(url, headers = header, data = data).text)
        warehouse = res['data']['warehouse_code']
        return warehouse

# 获取经纬度
def getLonLal(fir, sec, thir, forth):
    address = fir + sec + thir + forth
    url = "http://api.map.baidu.com/geocoder?address=" + address + "&output=json&key=X2xwG17XDfD7Bv1Ujip2riCQNUR30eLH"
    res = json.loads(requests.get(url).text)
    return res['result']['location']['lng'], res['result']['location']['lat']

# 四级地址信息
def getForth(first = '北京市', second = '北京市', third = '大兴区'):
    obj = getAddress()
    provincecode, provinceid, limit_line = obj.getAddr(first, '', 1)
    citycode, cityid, limit_line = obj.getAddr(second, provincecode, 1)
    areacode, areaid, limit_line = obj.getAddr(third, citycode, 1)
    forth = obj.getAddr('', areacode, 2)
    return forth

class submitOrder(getWare):
    # 提交订单按钮接口
    def getCanshu(self, provinceName, cityName, areaName, streetName, skucode, buyCount, phone, expect1, expect2, deliverWay, payType):
        # 得到用户信息
        customer_id, consumer_code = self.getCustomerInfo(phone)
        memberid = self.getMemberId(customer_id, phone)
        # 四级地址代码、id、限行
        provincecode, provinceid, limit_line = self.getAddr(provinceName, '', 1)
        citycode, cityid, limit_line = self.getAddr(cityName, provincecode, 1)
        areacode, areaid, limit_line = self.getAddr(areaName, citycode, 1)
        streetcode, streetid, limit_line = self.getAddr(streetName, areacode, 1)
        # 获取对应仓code
        warehouse = self.getStock(citycode, areacode)
        # 对应仓商品价格、id、小数位
        price, skuid, number_decimal = self.getWareInfo(customer_id, citycode, memberid, areacode, warehouse, skucode)

        data = self.getData(memberid, provinceid, provincecode, provinceName, cityid, citycode, cityName, areaid, areacode, areaName, streetid, streetcode, streetName,limit_line, price, skucode, skuid, number_decimal, customer_id, consumer_code, warehouse, buyCount, expect1, expect2, deliverWay, payType)

        # 发送请求
        url = '{}/api/pc/trade/cs/submitOrder'.format(self.host)
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        res = json.loads(requests.post(url, headers = header, data = json.dumps(data)).text)
        print(res)
        return limit_line, res['orderId']


    # 配置参数
    def getData(self, memberid, province_id, province_code, provinceName, city_id, city_code, cityName, district_id, district_code, areaName, street_id, street_code, streetName, limitLine, salePrice, skuCode, skuId, numberDecimal, customer_id, customer_code, warehouse, buyCount, expect1, expect2, deliverWay, payType):
        lng, lat = getLonLal(provinceName, cityName, areaName, streetName)
        data = {
            "boxId": '',
            "deliverWay": deliverWay,  # 物流方式 private-自有物流;kd-快递;ky-快运;car-专车包车;zt-自提
            "device_platform": "cs",  # 下单平台
            "couponModel": {    # 优惠券
                "couponCode": ""
            },
            "dispatchBillModel": None,
            "invoiceFlag": "10",   # 是否开发票  10不是 20是
            "invoiceTitle": None,  # 发票抬头
            "invoiceType": 20,     # 发票类型：10-增值税；20-普税
            "crmInvoiceId": None,  # 开票客户编码：默认空串
            "registerAddress": None,  # 注册地址
            "registerPhone": None,   # 注册电话
            "openBank": None,       # 开户行
            "bankAccount": None,    # 银行账户
            "ip": None,
            "memberId": memberid,  # 会员ID
            "payModel": {        # 支付方式
                "payName": "",   # 可以不传
                "payType": payType,  #账期1201, 在线 1001 银行1301 货到1101
                "paySubType": "",  # 子级支付编码，可不传
                "remark": None,
                "onoff": None,
                "accountAvailable": None
            },
            "qualityFileRequired": "20",  # 是否需要资质文件: 10-需要;20-不需求
            "receiveOnlyAt": 0,   # 时间段 0不限
            "remarks": "",   # 订单备注
            "separateShippingFee": "10",  # 是否单开运费: 10-是；20-否
            "shippingAddress": {
                "province_id": province_id,  # 省id
                "province_code": province_code, # 省编码
                "provinceName": provinceName, # 省名

                "city_id": city_id,        # 市id
                "city_code": city_code,  # 市编码
                "cityName": cityName,     # 市名

                "district_id": district_id,    # 区id
                "district_code": district_code, # 区编码
                "areaName": areaName,     # 区名

                "street_id": street_id,        # 街道id
                "street_code": street_code, # 街道编码
                "streetName": streetName,  # 街道名称

                "detail_address": "是", # 详细地址
                "ship_add_id": "",    # 地址ID  可以没有
                "warehouse_code": warehouse,  # 地址对应的仓
                "add_alias": "",        # 地址别名/自提点名称
                "office_phone": None,    # 固定电话/自提点联系方式
                "areaLimitLine": None,   # 限行，代客不取这个
                "limitLine": None,       # 限行 代客不取这个
                "email": None,
                "address_type": None,   # 地址类型：10=分销地址
                "is_default": None,
                "parent_warehouse_code": None,
                "address_source": 10,   # 地址来源：10-收货地址；20-自提地址
                "addressPersonList": [{
                    "id": None,
                    "addressId": None,
                    "status": None,
                    "receiverName": "测试收货人",   # 收货人姓名
                    "mobile": "15698708961",   # 电话
                    "receiverId": None,
                    "createTime": None
                }],
                "longitude": lng,   # 经度
                "latitude": lat,    # 纬度
                "temp_address": "10"         # 是否临时地址 10否  20是
            },
            "taxpayerIdentifyNum": None,   # 纳税人识别号
            "token": "",
            "wannaArrivedAtBegin": expect1,
            "wannaArrivedAtEnd": expect2,
            "mayArrivedIn": "",    # 第三方物流填，预计时间
            "warehouseId": None,
            "branchName": "大兴分公司",  # 分支机构
            "branchDepartment": "大兴配送部",  # 分支机构 部门
            "branchContacts": "杨广君",  # 分支机构联系人
            "branchPhone": "13581685237",  # 分支机构电话
            "loginAccount": "石凤刚",
            "roleName": "石凤刚",     # 下单客服的名字
            "roleId": "2000777",    # 下单客服id
            "changePriceRemark": "",  # 订单改价备注
            "adminChangeFreight": "",  # 是否修改运费
            "modifiyFreightReason": "",  # 修改运费原因
            "selfTakeTime": "",        # 自提时间
            "urgentTag": None,
            "limitLine": limitLine,         # 是否限行  10-限行；20-不限行
            "lastArrivedTime": "",   # 加急配送：最迟送达时间（多选一）
            "usedCoupon": "20",    # 使用优惠券:10-使用;20-未使用
            "skuModelList": [{
                "buyyerCount": buyCount,   # 购买数量（支持小数购买，类型：BigDecimal）
                "cartId": None,     # 购物车ID
                "salePrice": salePrice,  # 销售价格
                "skuCode": skuCode,
                "skuId": skuId,
                "skuName": None,
                "spuId": None,
                "adminChangePrice": "20",  # CS: 是否改价
                "joinPromotionTag": "20",  # 参与促销标记：10-参与；20-不参与（新增字段，默认传：10）
                "tempPurchase": "20",     # 临采商品: 10 - 是；20 - 否
                "activityId": "",         # 促销活动ID
                "promotionPrice": 0.0,     # 促销优惠金额
                "numberDecimal": numberDecimal       # 商品小数位
            }],
            "accountType": "10",    # 账号类型：10-签约；20-普通；30-认证
            "customer_id": customer_id,   # 项目ID(签约用户必传)
            "customer_code": customer_code,  # 项目编码(签约用户必传)
            "branchCrmId": 63,           # 分支结构对应CRM分公司ID
            "branchCrmName": "北京大兴分公司",  # 分支结构对应CRM分公司名称
            "requestSource": "10"        # 请求来源：10-配送；20-自提
        }
        return data



