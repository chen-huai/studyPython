# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

import smtplib
from email.mime.text import MIMEText # 邮件正文
from email.header import Header  # 邮件头

# 登录

smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
smtp_obj.login("nami@luffycity.com", "xxx")

# 设置邮件内容

mail_body = '''
    <h5>hello,小哥哥</h5>
    <p>
        小哥哥，约么？800，新到学生妹.. <a href="http://wx1.sinaimg.cn/mw1024/5ff6135fgy1gdnghz2vbsg205k09ob2d.gif"> 这是我的照片</a></p>
    </p>
'''

msg = MIMEText(mail_body, "html", "utf-8")

msg["From"] = Header("来自娜美的问候2020","utf-8") # 发送者
msg["To"] = Header("有缘人","utf-8") # 接收者
msg["Subject"] = Header("娜美的信2020","utf-8") # 主题

# 发邮件

smtp_obj.sendmail("xx@luffycity.com", ["xx","xx@qq.com"],msg.as_string())