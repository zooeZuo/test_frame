#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

import unittest
import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')


Base_Dir = os.path.dirname(os.path.realpath(__file__))
Test_Report_Dir = os.path.join(Base_Dir,'report')
Case_Dir = os.path.join(Base_Dir,'testcases')


#查找所有测试用例
discover = unittest.defaultTestLoader.discover(Case_Dir, pattern='test_*.py')

now = time.strftime('%Y-%m-%d_%H_%M_%S_')

#生成测试报告
filename = Test_Report_Dir + '\\' + now + 'result.html'
fp = open(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title='数据准备接口自动化测试报告',
                                       description='数据准备接口测试')

def new_file(testdir):
    #列出目录下所有文件
    lists = os.listdir(testdir)
    #文件排序
    lists.sort(key=lambda fn:os.path.getmtime(testdir+'\\'+fn))
    #获取最新文件
    file_path = os.path.join(testdir,lists[-1])

    return file_path

def send_email(newfile):
    #打开文件
    f = open(newfile,'rb')
    #读取文件内容
    #mail_body = f.read()

    f.close()

    #发送邮箱服务器
    smtpserver = 'pdc.fmsh.com.cn'
    #发送邮箱用户名/密码
    user = 'zuodengbo@fmsh.com.cn'
    password = '12250312'

    #发送邮箱
    sender = 'zuodengbo@fmsh.com.cn'

    #接收邮箱
    receiver = ['zooe.zuo@foxmail.com']

    #邮件主题
    subject = '测试报告'

    #正文内容
    msg = MIMEMultipart('mixed')

    #msg_html1 = MIMEText(mail_body,'html','utf-8')
    #msg.attach()

    #msg_html = MIMEText(mail_body,'html','utf-8')
    msg_html = MIMEText(open('%s'% filename,'rb').read(), 'base64', 'utf-8')
    msg_html['Content_Disposition'] = 'attachment;filename = "%s"'% filename
    msg.attach(msg_html)

    msg['From'] = 'zuodengbo@fmsh.com.cn'
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject,'utf-8')

    #连接发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,25)
        smtp.ehlo_or_helo_if_needed()
        smtp.login(user,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print('发送邮件成功')
    except TypeError:
        print('发送邮件失败')


if __name__=='__main__':

    print ('========AutoTest Start========')
    # 初始化测试起始时间
    start_time = datetime.datetime.now()

    #执行测试
    runner.run(discover)

    fp.close()

    #取最新测试报告
    new_report = new_file(Test_Report_Dir)


    #测试执行时间计算
    end_time = datetime.datetime.now()
    total_time = u'\t总共耗时：' +str((end_time - start_time).seconds)+ u'秒'

    # 发送邮件
    send_email(new_report)

    print('========AutoTest Over========')