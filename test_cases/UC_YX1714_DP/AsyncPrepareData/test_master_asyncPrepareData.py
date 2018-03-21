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


class NormalAsyncPrepareData(IRequest,RequestData):

    def test_asyncPrepareData(self):
        requestJsonDict = self.asyncPrepareDataScheme()

        response = self.asyncPrepareData_req(requestJsonDict)

        logging.debug('AsyncPrepareDataTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '00'