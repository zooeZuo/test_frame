#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

#from config.config import HTTP_OPTIONS,DEBUG_OPTIONS
from http_config import Http_Config
import unittest
import requests
import logging
import json as js
from log import logger


"""
This codes is used for request handle.

According to different request methods, there are different ways handle the requests,

and print the log.

"""
obj = Http_Config()
endpoint = obj.set_url()

class RequestHandle(unittest.TestCase):
    def setUp(self):
        log_level = logging.INFO
        log_level_option = 'DEBUG'
        if log_level_option == 'NOTSET':
            log_level = logging.NOTSET
        elif log_level_option == 'DEBUG':
            log_level = logging.DEBUG
        elif log_level_option == 'INFO':
            log_level = logging.INFO
        elif log_level_option == 'WARN':
            log_level = logging.WARN
        elif log_level_option == 'ERROR':
            log_level = logging.ERROR
        elif log_level_option == 'FATAL':
            log_level = logging.FATAL
        logging.basicConfig(level=log_level,
                            format='%(asctime)s %(filename)-12s line:%(lineno)-6s %(levelname)-6s %(message)s',
                            datefmt='[%d/%b/%Y %H:%M:%S]')

    #get请求方式

    @staticmethod
    def get(url):
        absolute_url = endpoint.rstrip('/') + '/' + url.lstrip('/')
        logger.debug('>>> Request URL: %s' % absolute_url)
        logger.debug('>>> Request Method: GET')

        res = requests.get(absolute_url)
        logger.debug('<<< Status Code: %s' % res.status_code)
        try:
            logger.debug('<<< Response content: \r\n %s' % js.dumps(js.loads(res.content),indent=2,ensure_ascii=False))
        except ValueError:
            logger.debug('<<< Response content: \r\n %s' % res.content)
        return res

    #post请求方式
    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        absolute_url = endpoint.rstrip('/') + '/' + url.lstrip('/')
        logger.debug('>>> Request URL: %s' % absolute_url)
        logger.debug('>>> Request Method: POST')
        if json:
            logger.debug('>>> Request MI: \r\n %s' % js.dumps(json, indent=2, ensure_ascii=False))
        elif data:
            logger.debug('>>> Request MI: \r\n %s' % data)
        else:
            logger.debug('>>> Request MI: \r\n None')

        my_header = {'Content_Type': 'application/json'}
        res = requests.post(absolute_url,json=json,data=data,headers=my_header,**kwargs)
        logger.debug('<<< Status Code: %s' % res.status_code)
        try:
            re = js.loads(res.content)
            logger.debug('<<< Response content: \r\n %s' % js.dumps(re,encoding='utf-8',indent=2,ensure_ascii=False))
            logger.debug('<<< resultCode: \r\n %s' % re['resultCode'])
        except ValueError:
            logger.debug('<<< Response content:\r\n %s' % res.content)
        return res

    def tearDown(self):
        pass