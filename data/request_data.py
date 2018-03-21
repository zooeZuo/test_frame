#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
from public.db_config import MySqlDB
from public.common import get_sql


class RequestData:
    global deviceInfo, ssdInfo, SRCBusinessCode, dpanCode, authenticationCode, \
        xmTransTime, xmTransNum, extra, spTransTime, spTransNum, results, \
        scriptsInstanceId, apduResultList

    sql = get_sql('test', 'mi_ap', '3')
    print(sql)
    db = MySqlDB()
    db.connect_db(sql)
    tem = db.get_one()

    deviceInfo = tem[1]
    ssdInfo = tem[2]
    SRCBusinessCode = tem[3]
    dpanCode = tem[4]
    authenticationCode = tem[5]
    xmTransTime = tem[6]
    xmTransNum = tem[7]
    extra = tem[8]
    spTransTime = tem[9]
    spTransNum = tem[10]
    results = tem[11]
    scriptsInstanceId = tem[12]
    apduResultList = tem[13]
    db.close_db()

    def __init__(self):
        pass

    # 查询产品信息列表

    def GetProductInformationListScheme(self):
        reqDict = {'xmTransTime': xmTransTime,
                   'xmTransNum': xmTransNum,
                   'extra': extra
                   }


        return reqDict

    # 查询资金账户

    def GetPrepaymentListScheme(self):
        reqDict = {'xmTransTime': xmTransTime,
                   'xmTransNum': xmTransNum,
                   'extra': extra
                   }


        return reqDict

    # 查询租赁业务列表
    def GetBusinessInformationListScheme(self):
        reqDict = {
            'deviceInfo': deviceInfo,
            'xmTransTime': xmTransTime,
            'xmTransNum': xmTransNum,
            'extra': extra
        }

        return reqDict

    # 查询租赁业务详细信息
    def GetBusinessDetailedInformationScheme(self):
        reqDict = {'deviceInfo': deviceInfo,
                   'SRCBusinessCode': SRCBusinessCode,
                   'xmTransTime': xmTransTime,
                   'xmTransNum': xmTransNum,
                   'extra': extra
                   }


        return reqDict

    # 业务申请
    def ApplyPendingBusinessScheme(self):
        reqDict = {'deviceInfo': deviceInfo,
                   'ssdInfo': ssdInfo,
                   'authenticationCode': authenticationCode,
                   'xmTransTime': xmTransTime,
                   'xmTransNum': xmTransNum,
                   'extra': extra
                   }

        return reqDict


if __name__ == '__main__':
    d = RequestData()
    d.ApplyPendingBusinessScheme()
