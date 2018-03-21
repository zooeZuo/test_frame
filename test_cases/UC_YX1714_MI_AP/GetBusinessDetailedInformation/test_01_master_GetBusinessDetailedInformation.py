#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2017/12/29
# discription :
# vision      :
# copyright   :All copyright reserved by FMSH company
#from unittest import skip

__author__ = 'zuodengbo'
import logging

from public.ap_http_handle import IRequest
from other_ways.data import RequestData
import json


class TestGetBusinessDetailedInformation(IRequest,RequestData):

    def test_master_GetBusinessDetailedInformation(self):
        requestJsonDict = self.GetBusinessDetailedInformationScheme()

        response = self.GetBusinessDetailedInformation_req(requestJsonDict)

        logging.debug('GetBusinessDetailedInformation Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '0000'