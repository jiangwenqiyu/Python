import requests
from json import loads, dumps
from lxml import etree
from re import sub
import pymysql

class conMysql(object):
    def connect(self):
        self.con = pymysql.connect(host='rm-2ze1o902w4bw8gzj8to.mysql.rds.aliyuncs.com',port=3306,user='produsupsys',password='YUE19930524',database = 'bjyxquery')
        self.cur = self.con.cursor()
        print('���ݿ����ӳɹ���')

    def close(self):
        self.cur.close()
        self.con.close()


class getInfo(conMysql):
    def __init__(self):
        self.connect()
        self.header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        self.data = dict()

    def getDate(self, billNo):
        url = 'http://10.4.181.166/querypush-traln/qps/qpswaybilltraceinternal/queryCurrentTraceByTrace_nos'
        self.data['trace_nos'] = billNo
        res = loads(requests.post(url, headers = self.header, data = self.data).text)
        return res[0]['postDate']


    def getDetail(self, billNo):
        # ��Ҫ�Ȼ�ȡ��ѯ���ҳ����Ӧ����������Ϣ��ʱ��
        date = self.getDate(billNo)
        fdate = date.split(' ')[0]
        bdate = date.split(' ')[1]
        url = 'http://10.4.181.166/querypush-traln/qps/qpswaybilltraceinternal/findmailinfo?traceNo={}&opTime={}%20{}&postDate={}%20{}'.format(billNo, fdate, bdate, fdate, bdate)
        res = requests.get(url).text
        html = etree.HTML(res)
        # ʵ�����ʷ�
        title1 = html.xpath('//tbody/tr[1]/td[1]/text()')[0]
        content1 = html.xpath('//tbody/tr[1]/td[2]/text()')
        if not content1 == []:
            content1 = sub('\n|\r| ','',content1[0])
        else:
            content1 = '������'
        print(title1)
        print(content1)
        # �����ʷ�
        title2 = html.xpath('//tbody/tr[1]/td[3]/text()')[0]
        content2 = html.xpath('//tbody/tr[1]/td[4]/text()')
        if not content2 == []:
            content2 = sub('\n|\r| ','',content2[0])
        else:
            content2 = '������'
        print(title2)
        print(content2)
        # ���۽��
        title3 = html.xpath('//tbody/tr[2]/td[1]/text()')[0]
        content3 = html.xpath('//tbody/tr[2]/td[2]/text()')
        if not content3 == []:
            content3 = sub('\n|\r| ','',content3[0])
            if content3 == '':
                content3 = '������'
        else:
            content3 = "������"
        print(title3)
        print(content3)
        # ���۷�
        title4 = html.xpath('//tbody/tr[2]/td[3]/text()')[0]
        content4 = html.xpath('//tbody/tr[2]/td[4]/text()')
        if not content4 == []:
            content4 = sub('\n|\r| ','',content4[0])
            if content4 == '':
                content4 = '������'
        else:
            content4 = "������"
        print(title4)
        print(content4)
        # �ʼ�����
        title5 = html.xpath('//tbody/tr[3]/td[1]/text()')[0]
        content5 = html.xpath('//tbody/tr[3]/td[2]/text()')
        if not content5 == []:
            content5 = sub('\n|\r| ','',content5[0])
        else:
            content5 = "������"
        print(title5)
        print(content5)
        # �ʼ���ע
        title6 = html.xpath('//tbody/tr[3]/td[3]/text()')[0]
        content6 = html.xpath('//tbody/tr[3]/td[4]/text()')
        if not content6 == []:
            content6 = sub('\n|\r| ','',content6[0])
        else:
            content6 = "������"
        print(title6)
        print(content6)
        # �ļ��ͻ�����
        title7 = html.xpath('//tbody/tr[4]/td[1]/text()')[0]
        content7 = html.xpath('//tbody/tr[4]/td[2]/text()')
        if not content7 == []:
            content7 = sub('\n|\r|\t| ','',content7[0])
        else:
            content7 = "������"
        print(title7)
        print(content7)
        # �ļ��ͻ�����
        title8 = html.xpath('//tbody/tr[4]/td[3]/text()')[0]
        content8 = html.xpath('//tbody/tr[4]/td[4]/text()')
        if not content8 == []:
            content8 = sub('\n|\r| ','',content8[0])
        else:
            content8 = "������"
        print(title8)
        print(content8)
        # �ļ��ͻ�����
        title9 = html.xpath('//tbody/tr[5]/td[1]/text()')[0]
        content9 = html.xpath('//tbody/tr[5]/td[2]/text()')
        if not content9 == []:
            content9 = sub('\n|\r| ','',content9[0])
        else:
            content9 = "������"
        print(title9)
        print(content9)
        # �ļ��ͻ��绰
        title10 = html.xpath('//tbody/tr[5]/td[3]/text()')[0]
        content10 = html.xpath('//tbody/tr[5]/td[4]/text()')
        if not content10 == []:
            content10 = sub('\n|\r| ','',content10[0])
        else:
            content10 = "������"
        print(title10)
        print(content10)
        # �ռ�������
        title11 = html.xpath('//tbody/tr[6]/td[1]/text()')[0]
        content11 = html.xpath('//tbody/tr[6]/td[2]/text()')
        if not content11 == []:
            content11 = sub('\n|\r| ','',content11[0])
        else:
            content11 = "������"
        print(title11)
        print(content11)
        # �ռ��˵绰
        title12 = html.xpath('//tbody/tr[6]/td[3]/text()')[0]
        content12 = html.xpath('//tbody/tr[6]/td[4]/text()')
        if not content12 == []:
            content12 = sub('\n|\r| ','',content12[0])
        else:
            content12 = "������"
        print(title12)
        print(content12)
        # �ռ��˵�ַ
        title13 = html.xpath('//tbody/tr[7]/td[1]/text()')[0]
        content13 = html.xpath('//tbody/tr[7]/td[2]/text()')
        if not content13 == []:
            content13 = sub('\n|\r| ','',content13[0])
        else:
            content13 = "������"
        print(title13)
        print(content13)
        # ��������
        title14 = html.xpath('//tbody/tr[8]/td[1]/text()')[0]
        content14 = html.xpath('//tbody/tr[8]/td[2]/text()')
        if not content14 == []:
            content14 = sub('\n|\r| ','',content14[0])
        else:
            content14 = "������"
        print(title14)
        print(content14)
        # �ڼ�Ʒ��
        title15 = html.xpath('//tbody/tr[8]/td[3]/text()')[0]
        content15 = html.xpath('//tbody/tr[8]/td[4]/text()')
        if not content15 == []:
            content15 = sub('\n|\r| ','',content15[0])
            if content15 == '':
                content15 = '������'
        else:
            content15 = "������"
        print(title15)
        print(content15)
        # �Ƿ��ִ
        title16 = html.xpath('//tbody/tr[9]/td[1]/text()')[0]
        content16 = html.xpath('//tbody/tr[9]/td[2]/text()')
        if not content16 == []:
            content16 = sub('\n|\r| ','',content16[0])
        else:
            content16 = "������"
        print(title16)
        print(content16)
        # ��ִ������
        title17 = html.xpath('//tbody/tr[9]/td[3]/text()')[0]
        content17 = html.xpath('//tbody/tr[9]/td[4]/text()')
        if not content17 == []:
            content17 = sub('\n|\r| ','',content17[0])
        else:
            content17 = "������"
        print(title17)
        print(content17)

        word = 'insert into tb_detail_info values(0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        args = (billNo, content1, content2, content3, content4, content5, content6, content7, content8, content9, content10, content11, content12, content13, content14, content15, content16, content17)
        self.cur.execute(word, args)
        self.con.commit()


def main():
    obj = getInfo()
    obj.getDetail('1125442329436')

if __name__ == '__main__':
    main()