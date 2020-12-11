import requests
import json

class backConfirm(object):
    host = 'https://t2.fsyuncai.com'
    # 支付金额
    def getMoney(self, orderid):
        url = '{}/api/admin/aorder/confirm/getBankInfo'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        data = {'order_id':str(orderid)}
        res = json.loads(requests.post(url, headers = header, data = data).text)
        return res['data']['paidAmount']

    # 确认收款
    def makesure(self, orderid):
        money = float(self.getMoney(orderid))
        print(money)
        url = '{}/api/admin/aorder/confirm/comfirmMoney'.format(self.host)
        header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Content-Type': 'application/json'}
        data = {'bus_id': str(orderid),
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

obj = backConfirm()
obj.makesure(88119379854)