#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/17
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import codecs
import configparser
from path import BaseDir,ConfigPath,LOG_PATH,REPORT_PATH

"""This class is for reading and getting config file default data"""

class ReadConfig:
    def __init__(self):
        f = open(ConfigPath)
        data = f.read()

        #remomve BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(ConfigPath,'w')
            files.write(data)
            files.close()
        f.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(ConfigPath,encoding='utf-8')

    #读取邮件配置
    def get_email(self,name):
        value = self.cf.get('EMAIL',name)
        return value

    #读取Http配置
    def get_http(self,name):
        value = self.cf.get('HTTP',name)
        return value

    #读取Headers配置
    def get_headers(self,name):
        value = self.cf.get('HEADERS',name)
        return value

    def set_headers(self,name,value):
        self.cf.get('HEADERS',name,value)
        with open(ConfigPath,'w+') as f:
            self.cf.write(f)

    #读取URL配置
    def get_url(self,name):
        value = self.cf.get('URL',name)
        return value

    #读取database配置
    def get_db(self,name):
        value = self.cf.get('MYSQLDB',name)
        return value


if __name__=='__main__':

    print BaseDir
    print ConfigPath
    print LOG_PATH
    print REPORT_PATH

    rc = ReadConfig()
    host = rc.get_db('host')
    mail = rc.get_email('user')
    print host
    print mail