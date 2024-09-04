"""
发邮件注意事项：
1. 发件人要打开SMTP服务；
2. 要了解发件邮箱的SMTP服务的连接方式，域名等；
3. From，to 要符合邮箱发件规范；
"""
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import base64

def main():

    # 请自行修改下面的邮件发送者和接收者
    sender = 'ljf9411@qq.com'

    sender_name = base64.b64encode('老枪'.encode('utf-8')).decode('utf-8')

    receivers = ['2224742726@qq.com']
    message = MIMEMultipart()
    # qq邮箱对头信息格式有要求，汉字必须转为base64 https://service.mail.qq.com/detail/124/995
    message['From'] = Header( f'"=?UTF-8?B?{sender_name}?=" {sender}')
    message['To'] = Header(f'Jack {receivers[0]}')

    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    message.attach(MIMEText('用Python发送邮件的示ddd例代码', 'plain', 'utf-8'))

    smtper = SMTP_SSL('smtp.qq.com', 465)
    smtper.login(sender, 'xyqcepmrnuomqbgejxxx')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()