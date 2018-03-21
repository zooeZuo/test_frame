#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import unittest
import os, time, datetime
import sys
import HTMLTestRunner
from public.mail import Email
# from util import send_email

reload(sys)
sys.setdefaultencoding('utf-8')

Base_Dir = os.path.dirname(os.path.realpath(__file__))
Test_Report_Dir = os.path.join(Base_Dir, 'report')
Case_Dir = os.path.join(Base_Dir, 'test_cases')

now = time.strftime('%Y-%m-%d_%H_%M_%S_')

file_name = Test_Report_Dir + '\\' + now + 'report.html'
fp = open(file_name, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title='接口自动化测试报告',
                                       description='接口测试')


def new_file(testdir):
    # 列出目录下所有文件
    lists = os.listdir(testdir)
    # 文件排序
    lists.sort(key=lambda fn: os.path.getmtime(testdir + '\\' + fn))
    # 获取最新文件
    file_path = os.path.join(testdir, lists[-1])

    return file_path


if __name__ == '__main__':

    print('===============Test Begin==============')
    start_time = datetime.datetime.now()

    suite_name = sys.argv[1]
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    pattern = ''

    try:
        print('Will run test cases os suite %s ' % suite_name)
        if suite_name == 'dp1':
            pattern = 'test_master_*.py'
        elif suite_name == 'dp2':
            pattern = 'test_exception_*.py'
        elif suite_name == 'dp':
            pattern ='test_[(master)(exception)]*.py'

        elif suite_name == '01':
            pattern = 'test_01_master_*.py'
        elif suite_name == '02':
            pattern = 'test_02_exception_*.py'
        elif suite_name == '03':
            pattern = 'test_03_doubt_*.py'
        elif suite_name == '04':
            pattern = 'test_04_failure_*.py'
        elif suite_name == '12':
            pattern = 'test_[(01_master)(02_exception)]*.py'
        elif suite_name == '123':
            pattern = 'test_[(01_master)(02_exception)(03_doubt)]*.py'
        elif suite_name == 'all':
            pattern = 'test_[(01)(02)(03)(04)]*.py'

        else:
            raise Exception('Suite: %s unknown or not support')

    except:
        pass

    test_cases = loader.discover(
        start_dir=Case_Dir,
        top_level_dir=Base_Dir,
        pattern=pattern
    )

    suite.addTests(test_cases)
    runner.run(suite)
    end_time = datetime.datetime.now()
    total_time = u'\t总共耗时：' + str((end_time - start_time).seconds) + u'秒'

    # 取最新测试报告
    new_report = new_file(Test_Report_Dir)

    # 发送邮件
    # send = Email()
    # send.send()

    print('===============Test Ended================')
