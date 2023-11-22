from email.mime.text import MIMEText #构建附件使用
from email.mime.multipart import MIMEBase,MIMEMultipart #构建基础邮件使用

mail_mul = MIMEMultipart()
#构建邮件正文
mail_text = MIMEText("Hello,i am xx",'plain','utf-8')
#把构建好的邮件正文附加入邮件中
mail_mul.attach(mail_text)

#构建附加
#构建附件，需要从本地读入附件
#打开一个本地文件
#以rb格式打开
with open("02.html","rb") as f :
    s = f.read()
    #设置附件的MIME和文件名
    m = MIMEText(s,'base64','utf-8')
    m['Content-Type'] = 'application/octet-stream'
    #需要注意
    #1，attachment 后分号为英文状态
    #2.filename 后面需要用引号包裹，注意与外面引号错开
    m["Content-Disposition"] = "'attachment;filename' = '02.html'"
    #添加刀MIMEMultipart
    mail_mul.attach(m)

    from_addr = "1579954422@qq.com"
    # 此处是经过申请设置后的授权码 ，不是qq邮箱密码
    from_pwd = "awdtexeoakcmghgc"

    # 收件人信息
    # 此处使用qq 邮箱，我给自己发送
    to_addr = "1579954422@qq.com"

    # 输入SMTP服务器地址
    # 此处根据不同的邮件服务商有所不同的值
    # 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
    # 腾讯qq邮箱的smtp地址是smtp.qq.com

    smtp_srv = "smtp.qq.com"

    try:
        import smtplib
        # 两个参数
        # 第一个是服务器地址，但一定是bytes格式，所以需要编码
        # 第二个参数是服务器的接受访问端口
        srv = smtplib.SMTP_SSL(smtp_srv.encode(), 456)  # SMTP协议默认端口25
        # 登陆邮箱发送
        srv.login(from_addr, from_pwd)
        # 发送邮件
        # 三个参数
        # 1，发送地址
        # 2，接受地址，必须是list形式
        # 3，发送内容，作为字符串发送
        srv.sendmail(from_addr, [to_addr], msg.as_string())
        str.quit()
    except Exception as e:
        print(e)
