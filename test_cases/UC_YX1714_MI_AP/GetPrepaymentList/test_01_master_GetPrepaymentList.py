#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/05
# discription :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import logging

from public.ap_http_handle import IRequest
from other_ways.data import RequestData

import json

class TestGetPrepaymentList(IRequest,RequestData):

    def test_master_GetPrepaymentList(self):
        requestJsonDict = self.GetPrepaymentListScheme()

        response = self.GetPrepaymentList_req(requestJsonDict)

        logging.debug('GetPrepaymentList Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '0000'