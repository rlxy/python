import smtplib
from email.mime.text import MIMEText
import urllib.request

import time
import json

def Data():
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t={}'.format(time.time())
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    response = urllib.request.Request(url=url,headers=headers)
    data = urllib.request.urlopen(response)
    data = data.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    data = data['data']['chinaTotal']['total']

    Corroborate = data['confirm']   #确诊
    Suspected = data['suspect']     #疑似
    Cure = data['heal']                 #治愈
    die = data['dead']                  #死亡

    t = '请各位小可爱保护好自己，勤洗手，少出门，出门一定一定一定要佩戴口罩，尽量不出门'
    end = '给我所有的朋友'
    date = time.ctime()
    a = '-'*20
    text = r'目前为止，已确诊病例：{}疑似病例：{}已治愈：{}死亡病例：{}{}{}{}{}{}{}'.format(Corroborate,Suspected,Cure,die,a,t,a,date,a,end)
    print(text)
    return text

def email(Data,QQ):
    msg = MIMEText(Data,"html","UTF-8")

    from_addr = "1579954422@qq.com" #我方邮箱

    from_pwd = "avbflkhfnsxphhhj"

    to_addr = "{}@qq.com".format(QQ) #目标邮箱

    smtp_srv = "smtp.qq.com"
    msg['Subject'] = '请查收今日邮件哦'  #题目标题
    msg['From'] = from_addr
    msg['To'] = to_addr
    try:

        server = smtplib.SMTP(smtp_srv,25)   #SMTP协议默认端口25

        server.set_debuglevel(1)  #打印发送邮箱的过程

        server.login(from_addr,from_pwd)

        server.sendmail(from_addr,[to_addr],msg.as_string())
        server.quit()
    except Exception as e:
        print('error:',e)
if __name__ == '__main__':
    Data()
    data = Data()
    number = ('1579954422','3388253455')
    # email(data,'1579954422')


    ##得出结论，，邮件发多了会被禁止。。。。。