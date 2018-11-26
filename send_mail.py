# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from smtplib import  SMTP
def send_email(SMTP_host="smtp.163.com",
               from_account="shwb95@163.com",
               from_passwd="***",
               to_account="584927688@qq.com",
               title="CoinCola", content=None):
    email_client = SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()

if __name__ == '__main__':
    send_email(title="",content="Python 邮件发送测试...")
