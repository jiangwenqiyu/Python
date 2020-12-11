from locust import TaskSet, task, HttpUser, between
import os

class USER(HttpUser):
    host = 'https://t4.fsyuncai.com'
    wait_time = between(1,5)

    def on_start(self):
        pass

    @task(1)
    def u_post(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Cookie': 'cityCode=1; provinceCode=1; wareHouseCode=1; Hm_lvt_47bc68128fb7e2190a5f2966d6a30000=1599888138; UM_distinctid=17480c39f0d57b-04e51a9b1d4778-3f6b4b05-15f900-17480c39f0e414; CNZZDATA1274765129=2066623448-1599888126-%7C1599888126; registerSource=10; accountType=20; loginAccount=ndiucf168353; memberId=166333; token=4081983133e7748840a75d75693e690e; lgdomain=t4; dialogStatus=6'}
        url = '/tmsStatic/?m_tk=272dtowiXfDhmFGNJ03+HAfYUbyPd1BhrBotRPGbnNExBQRdIiPzJmSx1BJfaYlrW5i9LtARR89MSidRjO5GZDIoHlCuZ5h/BAFR9j16LuxKwzwHGNMeLM66S+IjKXNG7eZSUSaDFtnM02ZoR5k'
        a = self.client.get(url, headers=header, name='打开').text
        # print(a)

if __name__ == '__main__':
    os.system('locust -f locust-worker.py --worker --master-host=192.168.66.238')





