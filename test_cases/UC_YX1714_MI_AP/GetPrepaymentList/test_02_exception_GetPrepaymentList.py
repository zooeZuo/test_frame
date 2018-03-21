#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2017/12/29
# discription :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import logging
import json
from public.ap_http_handle import IRequest
from other_ways.data import RequestData

class TestGetPrepaymentList(IRequest,RequestData):

    #参数缺失类型
    def test_exception_GetPrepaymentList_param_miss_01(self):
        requestJsonDict = self.GetPrepaymentListScheme()

        requestJsonDict.pop('xmTransTime')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_miss_02(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransTime='')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_miss_03(self):
        requestJsonDict = self.GetPrepaymentListScheme()

        requestJsonDict.pop('xmTransNum')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_miss_04(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransNum='')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'


    #参数非法类型
    def test_exception_GetPrepaymentList_param_illegal_01(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransTime='交易时间')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_illegal_02(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransTime='asdfghjkl')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_illegal_03(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransTime='1234#%。56.')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_illegal_04(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransNum='交易处理号')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_illegal_05(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransNum='asdfghjkl')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'

    def test_exception_GetPrepaymentList_param_illegal_06(self):
        requestJsonDict = self.GetPrepaymentListScheme(xmTransNum='1234#%。56.')

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s', response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '4002'