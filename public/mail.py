#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/2
# discription :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

"""
邮件类。用来给指定用户发送邮件。可指定多个收件人，可带附件。
"""
import re,os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
import threading
from public.log import Logger
from utils import read_config
import path
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

local = read_config.ReadConfig()
log = Logger()
logger = log.get_logger()


class Email:
    def __init__(self):
        """初始化Email

        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        :param server: smtp服务器，必填。
        :param sender: 发件人，必填。
        :param password: 发件人密码，必填。
        :param receiver: 收件人，多收件人用“；”隔开，必填。
        """
        self.title = local.get_email('subject')
        self.message = local.get_email('content')
        self.files = self.new_file(path.REPORT_PATH)

        self.msg = MIMEMultipart('related')

        self.server = local.get_email('server')
        self.port = local.get_email('port')
        self.sender = local.get_email('sender')
        self.receiver = local.get_email('receiver')
        self.password = local.get_email('password')

    def new_file(self,report):
        """find the newest report file"""
        # 列出目录下所有文件
        lists = os.listdir(report)
        # 文件排序
        lists.sort(key=lambda fn: os.path.getmtime(report + '\\' + fn))
        # 获取最新文件
        file_path = os.path.join(report, lists[-1])

        return file_path


    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]  # 查找最后一个测试报告作为附件
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title  # 主题
        self.msg['From'] = self.sender  # 发送方
        self.msg['To'] = self.receiver  # 接收方

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server,self.port)  # 连接sever
        except (gaierror and error) as err:
            logger.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', err)
        else:
            try:
                smtp_server.login(self.sender, self.password)  # 登录
            except smtplib.SMTPAuthenticationError as err:
                logger.exception('用户名密码验证失败！%s', err)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
            finally:
                smtp_server.quit()  # 断开连接
                logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == '__main__':
    #report = 'D:\\test_frame\\log\\log.txt'.encode('utf-8')
    e = Email()
    e.send()
