#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
from request_handle import RequestHandle
from log import logger
import threading
from common import get_url_from_xml

class IRequest(RequestHandle):
    mutex = threading.Lock()
    mutex.acquire()


    # MI_AP
    # 查询资金账户
    def GetPrepaymentList_req(self, requestJsonData):
        url = get_url_from_xml('GPL')
        response = self.post(url, json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response

    # 查询产品信息列表
    def GetProductInformationList_req(self, requestJsonData):
        url = get_url_from_xml('GPIL')
        response = self.post(url, json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response


    # 查询租赁业务列表
    def GetBusinessInformationList_req(self, requestJsonData):
        url = get_url_from_xml('GBIL')
        response = self.post(url, json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response


    # 查询租赁业务详细信息
    def GetBusinessDetailedInformation_req(self, requestJsonData):
        url = get_url_from_xml('GBDI')
        response = self.post(url, json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response



    # 业务申请
    def ApplyPendingBusiness_req(self, requestJsonData):
        url = get_url_from_xml('APB')
        response = self.post(url, json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response


    # 告知业务结果
    def NotifyBusinessResults_req(self, requestJsonData):
        response = self.post('/NotifyBusinessResults', json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response


    # 反向业务推送
    def SubmitBusiness_req(self, requestJsonData):
        url = get_url_from_xml('SB')
        response = self.post(url, json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response

    #内部MQ
    def PostScriptResults_req(self, requestJsonData):
        url = get_url_from_xml('PSR')
        response = self.post(url, json=requestJsonData)
        logger.debug('>>> Response.status_code: \r\n %s' % response.status_code)
        return response