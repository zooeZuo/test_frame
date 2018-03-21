#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import logging,json

from public.dp_http_handle import IRequest
from other_ways.data import RequestData


class QueryPrepareDataResultExceptionTestCase(IRequest,RequestData):
    def test_queryPrepareDataResult_null_01(self):

        requestJsonDict = self.queryPrepareDataResultScheme()

        requestJsonDict.pop('serviceCode')

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_queryPrepareDataResult_null_02(self):
        requestJsonDict = self.queryPrepareDataResultScheme()

        requestJsonDict.pop('sn')

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s', response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_queryPrepareDataResult_type_change_01(self):
        requestJsonDict = self.queryPrepareDataResultScheme(serviceCode=-2)

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_queryPrepareDataResult_type_change_02(self):
        requestJsonDict = self.queryPrepareDataResultScheme(sn=-2)

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_queryPrepareDataResult_length_illegal_01(self):
        requestJsonDict = self.queryPrepareDataResultScheme(serviceCode='11111111111111111111111111111111111')

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_queryPrepareDataResult_length_illegal_02(self):
        requestJsonDict = self.queryPrepareDataResultScheme(sn='11111111111111111111111111111111111')

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_queryPrepareDataResult_illegal_chars_01(self):
        requestJsonDict = self.queryPrepareDataResultScheme(serviceCode='7+-\*/7%')

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'

    def test_queryPrepareDataResult_illegal_chars_02(self):
        requestJsonDict = self.queryPrepareDataResultScheme(sn='7e+-\*/7%')

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content

        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '01'