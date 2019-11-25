# 发邮件
from email.mime.text import MIMEText
from email.header import Header
from QiYeWeiXinAutoTest.common.Mylogger import logger
from QiYeWeiXinAutoTest.common.DoYml import readYml
import smtplib
import os


def sendMail(reportPath):

    # 发送邮件配置，稍后改成从配置文件中读取



    MailConfigPath = os.path.join(os.path.dirname(os.path.dirname(__file__)),  './config/mail_config.yml')
    mailconfig = readYml(MailConfigPath)

    logger.info(mailconfig)
    logger.info(type(mailconfig))
    smtpserver = mailconfig['baseicConfig']['smtpserver']
    user = mailconfig['baseicConfig']['user']
    password = mailconfig['baseicConfig']['password']
    sender = mailconfig['baseicConfig']['sender']
    receiver = mailconfig['baseicConfig']['receiver']
    subject = mailconfig['baseicConfig']['subject']

    # 将报告内容提取出来
    fopen = open(reportPath,'rb')
    mailbody = fopen.read()
    fopen.close()

    # 将报告内容转换成html格式
    msg = MIMEText(mailbody,'html','utf-8')
    msg["Subject"] = Header(subject,'utf-8')

    # 发邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    logger.info("已将测试报告发送到相关人员邮箱~！")
    smtp.quit()


