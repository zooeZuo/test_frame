#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/2
# discription :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import logging
from logging.handlers import TimedRotatingFileHandler
import threading
import configparser
import os
from utils.read_config import LOG_PATH, REPORT_PATH


class Logger(object):

    def __init__(self):
        # 上锁，防止多线程下出问题
        mutex = threading.Lock()
        mutex.acquire()
        config = configparser.ConfigParser()
        config.read('D:/test_frame/config/log_config.conf', encoding='utf-8')
        sec = config.sections()
        print sec
        self.log_filename = config.get('LOGGING', 'log_file')  # 日志文件名
        self.max_bytes = int(config.get('LOGGING', 'max_bytes_each'))  # 日志文件最大字节数
        self.backup_count = int(config.get('LOGGING', 'backup_count'))  # 日志保留数量
        self.format = config.get('LOGGING', 'format')  # 日志打印格式
        self.console_log_level = int(config.get('LOGGING', 'console_log_level'))  # 控制台日志级别
        self.logfile_log_level = int(config.get('LOGGING', 'logfile_log_level'))  # 日志文件日志级别
        self.logger_name = config.get('LOGGING', 'logger_name')  # 日志打印名
        self.console_log_on = int(config.get('LOGGING', 'console_log_on'))  # 是否开启控制台日志打印
        self.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))  # 是否开启文件日志打印
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(10)
        mutex.release()

    def get_logger(self):
        """
        在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        我们这里添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
        两个句柄的日志级别不同，在配置文件中可设置。
        """
        # 设置日志格式
        format = self.format.replace('|', '%')  # 用%替换|
        formatter = logging.Formatter(format)

        if self.console_log_on == 1:  # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            console.setLevel(self.console_log_level)
            self.logger.addHandler(console)
            print(self.logger.getEffectiveLevel())

        if self.logfile_log_on == 1:  # 如果开启文件日志
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_filename),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(formatter)
            file_handler.setLevel(self.logfile_log_level)
            self.logger.addHandler(file_handler)
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :param case_no:
        :return:
        """
        self.logger.info('--------' + case_no + 'START--------')

    def build_end_line(self, case_no):
        """
        write end line
        :param case_no:
        :return:
        """
        self.logger.info('--------' + case_no + 'END--------')

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info(case_name + '- Code: ' + code + '- msg: ' + msg)

    @staticmethod
    def get_log_path():
        """
        get test log path
        :return:
        """
        return LOG_PATH


    def get_report_path(self,report_dir):
        """
        get report file path
        :return:
        """
        lists = os.listdir(report_dir)
        lists.sort(key=lambda fn: os.path.getmtime(report_dir + '\\' + fn))
        report_path = os.path.join(REPORT_PATH, lists[-1])
        return report_path

    @staticmethod
    def write_results(result):
        """
        write test result
        :param result:
        :return:
        """
        result_path = os.path.join(LOG_PATH, 'log.txt')
        f = open(result_path, 'wb')
        try:
            f.write(result)
        except Exception as e:
            logger.error(str(e))


logger = Logger().get_logger()

if __name__ == '__main__':
    logger.debug(u'牛逼')
