import requests
import json


def judgeArrive(billNum):
    url = 'https://t4.fsyuncai.com/tmspc/saleOrder/saleOrderList'
    header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
              'Content-Type': 'application/json'}

    data = {
        "pageNum": 1,
        "pageSize": 10,
        "sortObject": {
            "sortKey": 0,
            "sortValue": 0
        },
        "deliveryMethod": "1",
        "companyId": 257938,
        "authQuery": "(((s.bill_type in (1,2,3,7) and s.delivery_company_id = 257938) or (s.bill_type in (4,5,3,8) and s.handle_company_id = 257938)))",
        "latestDeliveryTime": None,
        "saleBillNo": None,
        "dispatcherBillNo": None,
        "inCompanyId": None,
        "billIds": None,
        "provinceId": "",
        "cityId": "",
        "areaId": "",
        "advancedQueryList": [{
            "concatSymbol": "and",
            "bracketLeft": "",
            "controlType": "10",
            "frontName": "运单号",
            "compareSymbol": "=",
            "bracketRight": "",
            "controlHasCandidate": 0,
            "value": billNum,
            "dataType": "10",
            "controlCandidateValue": "",
            "dbName": "s.sale_bill_no",
            "sequence": 0,
            "showType": 0
        }],
        "isUrgent": 0,
        "isLimit": 0,
        "isLack": 0,
        "isIncludeSpecial": 0,
        "isRefund": 0,
        "isIncludeMutex": 0,
        "wareHouseId": None,
        "isChangeCompany": 0,
        "isInclude9999": 2,
        "differenceSplitOrder": 0,
        "routeKey": None,
        "weightLoad": None,
        "volumeLoad": None,
        "saleBillId": None,
        "distance": None,
        "billStatus": 1,
        "recoverQuery": 0
    }
    res = json.loads(requests.post(url, headers = header, data = json.dumps(data)).text)
    if res['data']['data'] == []:
        print('单据没到达TMS！')
    else:
        billId = res['data']['data'][0]['saleBillId']
        url = 'https://t4.fsyuncai.com/tmspc/saleOrder/pickingAllow'
        data = {
            "confirmPush": 1,
            "id": 0,
            "orderBillIdList": [billId],
            "companyId": 257938,
            "confirmAreaPush": 1
        }
        res = json.loads(requests.post(url, headers = header, data = json.dumps(data)).text)
        if res['msg'] == '操作成功':
            print('允许拣货完成！')

def main():
    judgeArrive('66103305301')

if __name__ == '__main__':
    main()


