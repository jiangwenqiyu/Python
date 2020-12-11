import pymysql
import tkinter
import threading
import random

def makeMobile():
    connect = pymysql.connect(host='192.168.0.27', port = 3306, user = 'developer', password = 'dev_123', database = 'xfs_membership')
    cur = connect.cursor()

    while True:
        # 生成手机号
        head = ['135','136','155','177','159','188','133']
        body = random.randint(10000000,99999999)
        num = random.choice(head) + str(body)
        # 检查是否重复
        checkWord = 'select mobile_phone from member where mobile_phone={}'.format(num)
        cur.execute(checkWord)
        data = cur.fetchone()
        if data == None:
            break
        else:
            continue
    e1.delete(0,len(e1.get()))
    e1.insert(0,num)
    cur.close()
    connect.close()

def querry():
    connect = pymysql.connect(host='192.168.0.27', port = 3306, user = 'developer', password = 'dev_123', database = 'xfs_membership')
    cur = connect.cursor()

    word = 'select veryfy_code from verify_code where mobile={}'.format(e1.get())
    cur.execute(word)
    data = cur.fetchall()
    e2.delete(0,len(e2.get()))
    try:
        e2.insert(0, data[-1][0])
    except:
        e2.insert(0,data[0][0])
    cur.close()
    connect.close()

def thQuerry(state):
    if state == '验证码':
        t = threading.Thread(target=querry)
        t.start()
    else:
        t = threading.Thread(target=makeMobile)
        t.start()

gui = tkinter.Tk()
gui.geometry('400x200+700+350')
e1 = tkinter.Entry(gui)
e1.place(relx = 0.2, rely = 0.2)
e2 = tkinter.Entry(gui)
e2.place(relx = 0.2, rely = 0.6)
btn1 = tkinter.Button(gui, text = '查询验证码', command = lambda :thQuerry(btn1.widgetName))
btn1.widgetName = '验证码'
btn1.place(relx = 0.6, rely = 0.45)
btn2 = tkinter.Button(gui, text = '获取手机号', command = lambda :thQuerry(btn2.widgetName))
btn2.widgetName = '手机号'
btn2.place(relx = 0.6, rely = 0.25)
gui.mainloop()

