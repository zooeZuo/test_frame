#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

"""
There are some default configuration about url,log level.

By invoking it's Synonym handling relevant data interface.
"""

HTTP_OPTIONS = {
    #'endpoint':'http://192.168.39.10:8080/dp'
    'endpoint':'http://192.168.110.179:7001/SHSRC/MI/business/1/1'
    # 'client_cert_path':'',
    # 'client_key_path':'',
    # 'should_verify_server_cert':False,
}

DEBUG_OPTIONS = {
    'log_level':'DEBUG',
}

DATABASE = {
    'host':'192.168.110.165',
    'port':'1521',
    'db':'ORCL',
    'username':'c##src_qa',
    'password':'sr2018qa'
}

REDIS = {
    'database':'11',
    'password':'qaredis',
    'sentinel':{
        'master':'mymaster',
        'node1':'192.168.39.57:26379',
        'node2':'192.168.39.110:26379'
    }
}

CASE_ID = 1
CASE_NAME = 2
CASE_METHOD = 4
CASE_URL = 5
CASE_DATA = 6
CASE_CODE = 7