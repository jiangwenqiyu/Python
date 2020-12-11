import re
import hashlib

# sign就是把data去掉第一层空值,然后按照顺序（字母或者数字）排序，转成key=value&key=value的字符串，最后+SECRET=XFS7ALC74OCVPHXG97ETTS
def generateSign(data):
    del data['sign']
    # 去除空值
    tm_k = []
    for i in data:
        if data[i] == "":
            tm_k.append(i)
    for i in tm_k:
        del data[i]
    # 排序
    temp_keys = sorted(data.keys())

    # 拼接成字符串
    temp_str = ''
    for i in temp_keys:
        temp_str += i + '=' + str(data[i]) + '&'
    temp_str += 'SECRET=XFS7ALC74OCVPHXG97ETTS'

    # 替换空格、引号、时间补全空格、null、全部设置大写
    temp_str = temp_str.replace(' ','')
    temp_str = temp_str.replace("'",'"')
    temp_str = temp_str.replace('None','null')
    # 处理时间
    time_list = []
    all_time = re.findall('\d+-\d+-\d+:\d+:\d+', temp_str)
    if not all_time == []:
        for t in all_time:
            sub_time = t[0:10]
            if not sub_time in time_list:
                temp_str = temp_str.replace(sub_time, sub_time + ' ')
                time_list.append(sub_time)
    temp_str = temp_str.upper()

    # 转md5
    md5 = hashlib.md5()
    md5.update(temp_str.encode('utf-8'))
    sign = md5.hexdigest()
    # 返回
    return sign