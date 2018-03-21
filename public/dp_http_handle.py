#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'zuodengbo'

"""
This codes is used for dealing with interface endpoints

and responding the status_code,judging if the interface points are normal. 
"""

from request_handle import RequestHandle
from log import logger
import threading
from common import get_url_from_xml

class IRequest(RequestHandle):
    mutex = threading.Lock()
    mutex.acquire()
    #DP
    #异步数据准备请求地址
    def asyncPrepareData_req(self, requestJsonData):
        url = get_url_from_xml('APD')
        response = self.post(url,json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response

    #查询数据准备结果请求地址
    def queryPrepareDataResult_req(self, requestJsonData):
        url = get_url_from_xml('QPDR')
        response = self.post(url,json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response





