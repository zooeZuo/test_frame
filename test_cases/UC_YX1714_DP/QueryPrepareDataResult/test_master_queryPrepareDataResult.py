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


class NormalQueryPrepareDataResult(IRequest,RequestData):
    def test_queryPrepareDataResult(self):

        requestJsonDict = self.queryPrepareDataResultScheme()

        response = self.queryPrepareDataResult_req(requestJsonDict)

        logging.debug('QueryPrepareDataResultTestCase Result >>> %s',response)

        r = response.content
        r = json.loads(r)

        assert (response.status_code == 200)
        assert r['resultCode'] == '00'