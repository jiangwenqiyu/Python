#coding=utf-8
import tkinter
import tkinter.ttk
import submit
from tkinter.messagebox import *
import threading

def getdeliverWay():
    typee = ComboBox_23.get()

    if typee == "鑫方盛物流":
        code = 'private'
    elif typee == "快递":
        code = 'kd'
    elif typee == "快运":
        code = 'ky'
    elif typee == "专车包车":
        code = 'car'
    return code

def getpayType():
    #账期1201, 在线 1001 银行1301 货到1101
    if ComboBox_22.get() == '银行转账':
        code = 1301
    elif ComboBox_22.get() == '账期支付':
        code = 1201
    elif ComboBox_22.get() == '在线支付':
        code = 1001
    elif ComboBox_22.get() == '货到付款':
        code = 1101
    return code

def sub():
    try:
        # 先清空限行和单号内容
        Entry_29.delete(0, len(Entry_29.get()))
        Entry_27.delete(0, len(Entry_27.get()))
        # 配送方式
        deliverWay = getdeliverWay()
        # 付款方式
        payType = getpayType()
        # 一级地址
        first = Entry_5.get()
        # 二级地址
        second = Entry_6.get()
        # 三级地址
        third = Entry_7.get()
        # 四级地址
        forth = ComboBox_8.get()
        # 商品编码
        skucode = Entry_17.get()
        # 数量
        skunum = int(Entry_18.get())
        # 客户手机号
        phone = Entry_3.get()
        # 期望送货时间
        expect1 = Entry_13.get()
        expect2 = Entry_14.get()

        obj = submit.submitOrder()
        limit, bill = obj.getCanshu(first, second, third, forth, skucode, skunum, phone, expect1, expect2, deliverWay, payType)

        Entry_29.insert(0, limit)
        Entry_27.insert(0, bill)

        showinfo('成功', message='制作成功')
    except Exception as e:
        showerror('报错', message=str(e))

def showStreet():
    streets = submit.getForth(Entry_5.get(), Entry_6.get(), Entry_7.get())
    ComboBox_8['value'] = tuple(streets)
    ComboBox_8.current(0)

def btnFunction(btn):
    if btn.widgetName == '地址':
        t = threading.Thread(target=showStreet)
        t.start()
    elif btn.widgetName == '提交订单':
        t = threading.Thread(target=sub)
        t.start()

if  __name__ == '__main__':
    root = tkinter.Tk()
    root.title("None")
    root.geometry("537x344")
    Form_1= tkinter.Canvas(root,width = 10,height = 4)
    Form_1.place(x = 0,y = 0,width = 537,height = 344)
    Form_1.configure(bg = "#efefef")

    Label_2= tkinter.Label(root,text="客户手机号:",width = 10,height = 4,font = 10)
    Label_2.place(x = 0,y = 12,width = 100,height = 30)

    Entry_3= tkinter.Entry(root,font = 10)
    Entry_3.place(x = 104,y = 17,width = 120,height = 20)

    Label_4= tkinter.Label(root,text="选择地址:",width = 10,height = 4, font = 10)
    Label_4.place(x = 13,y = 64,width = 68,height = 20)

    Entry_5= tkinter.Entry(root,font = 10)
    Entry_5.place(x = 103,y = 61,width = 67,height = 20)

    Entry_6= tkinter.Entry(root,font = 10)
    Entry_6.place(x = 177,y = 60,width = 67,height = 20)

    Entry_7= tkinter.Entry(root,font = 10)
    Entry_7.place(x = 251,y = 60,width = 72,height = 20)

    ComboBox_8= tkinter.ttk.Combobox(root,font = 10)
    ComboBox_8.place(x = 331,y = 59,width = 122,height = 20)

    Button_9= tkinter.Button(root,text="获取地址",width = 10,height = 4, command = lambda:btnFunction(Button_9))
    Button_9.place(x = 462,y = 55,width = 55,height = 28)
    Button_9.widgetName = '地址'

    Label_10= tkinter.Label(root,text="该地址是否限行",width = 10,height = 4, font = 10)
    Label_10.place(x = 85,y = 92,width = 130,height = 20)

    Label_12= tkinter.Label(root,text="期望送货时间:",width = 10,height = 4, font = 10)
    Label_12.place(x = 4,y = 125,width = 100,height = 20)

    Entry_13= tkinter.Entry(root,font = 10)
    Entry_13.place(x = 107,y = 125,width = 162,height = 20)

    Entry_14= tkinter.Entry(root,font = 10)
    Entry_14.place(x = 107,y = 162,width = 163,height = 20)

    Label_15= tkinter.Label(root,text="商品代码:",width = 10,height = 4, font = 10)
    Label_15.place(x = 298,y = 124,width = 70,height = 20)

    Label_16= tkinter.Label(root,text="数量:",width = 10,height = 4, font = 10)
    Label_16.place(x = 319,y = 162,width = 43,height = 20)

    Entry_17= tkinter.Entry(root,font = 10)
    Entry_17.place(x = 363,y = 124,width = 55,height = 20)

    Entry_18= tkinter.Entry(root,font = 10)
    Entry_18.place(x = 362,y = 162,width = 36,height = 20)

    Label_20= tkinter.Label(root,text="支付方式:",width = 10,height = 4, font = 10)
    Label_20.place(x = 31,y = 203,width = 73,height = 20)

    Label_21= tkinter.Label(root,text="配送方式:",width = 10,height = 4, font = 10)
    Label_21.place(x = 262,y = 205,width = 75,height = 20)

    ComboBox_22= tkinter.ttk.Combobox(root,textvariable=tkinter.StringVar(), font = 10)
    ComboBox_22.place(x = 109,y = 203,width = 100,height = 20)
    ComboBox_22['value'] = ('银行转账', '账期支付', '在线支付', '货到付款')
    ComboBox_22.current(0)  #账期1201, 在线 1001 银行1301 货到1101

    ComboBox_23= tkinter.ttk.Combobox(root,textvariable=tkinter.StringVar(), font = 10)
    ComboBox_23.place(x = 337,y = 206,width = 100,height = 20)
    ComboBox_23['value'] = ('鑫方盛物流', '快递', '快运', '专车包车')
    ComboBox_23.current(0)

    ComboBox_24= tkinter.ttk.Combobox(root,textvariable=tkinter.StringVar(), font = 10)
    ComboBox_24.place(x = 339,y = 15,width = 100,height = 20)

    Label_25= tkinter.Label(root,text="订单类型:",width = 10,height = 4, font = 10)
    Label_25.place(x = 248,y = 17,width = 76,height = 20)

    Button_26= tkinter.Button(root,text="提交订单",width = 10,height = 4, command = lambda :btnFunction(Button_26))
    Button_26.place(x = 340,y = 255,width = 77,height = 28)
    Button_26.widgetName = '提交订单'

    Entry_27= tkinter.Entry(root,font = 10)
    Entry_27.place(x = 171,y = 258,width = 120,height = 20)

    Label_28= tkinter.Label(root,text="生成的单号:",width = 10,height = 4, font = 10)
    Label_28.place(x = 67,y = 259,width = 85,height = 20)

    Entry_29= tkinter.Entry(root,font = 10)
    Entry_29.place(x = 210,y = 91,width = 56,height = 20)

    Entry_3.insert(0, '13216542387')

    Entry_5.insert(0,'北京市')
    Entry_6.insert(0,'北京市')
    Entry_7.insert(0,'大兴区')

    Entry_17.insert(0,'021238')
    Entry_18.insert(0,1)

    Entry_13.insert(0, '2020-11-24 10:10:10')
    Entry_14.insert(0, '2020-11-25 10:10:10')
    root.mainloop()
