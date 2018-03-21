#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/3
# discription :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'


#http状态码及响应消息
class HttpStatus(object):
    NO_ERROR = '200'
    SYSTEM_ERROR = '500'
    SYSTEM_TEMP_ERROR = '503'
    BAD_REQUEST = '400'
    AUTH_FAILED = '401'
    NOT_FOUND = '404'

    RETRY_WITH_URL = '308'

    status_dictionary = {
        NO_ERROR: 'Http Status Ok ! ',
        SYSTEM_ERROR: 'System Error ! ',
        SYSTEM_TEMP_ERROR: 'System Temporary Error!',
        BAD_REQUEST: 'Bad Request!',
        AUTH_FAILED: 'Authentication Failed!',
        NOT_FOUND: 'Not Found ! '
    }

    @staticmethod
    def get_description(status_code):
        return HttpStatus.status_dictionary[status_code]

#测试返回结果状态码
class ResultCode(object):
    SUCCESS = '0000'
    FAILD = '1000'
    NO_PERSONAL_DATA = '2000'
    REQUIRE_DELETE_OLD_CARD = '2001'
    PERSONAL_FAILD = '2002'
    MESSAGE_FORMAT_ERROR = '4002'
    SYSTEM_ERROR = '4003'
    APP_OR_SESSION_NOT_CHANGE = '4005'
    SCRIPT_SUCCESS = '6310'
    ORDER_STATUS_NOT_SURE = '9000'
    ORDER_NON_EXISTENT = '9001'


    message_dict = {
        SUCCESS:'Successful and no subsequent script !',
        FAILD:'Failure !',
        NO_PERSONAL_DATA:'No personalization data was found !',
        REQUIRE_DELETE_OLD_CARD:'Need to delete old cards !',
        PERSONAL_FAILD:'Personal failure !',
        MESSAGE_FORMAT_ERROR:'Error message format !',
        SYSTEM_ERROR:'System error !',
        APP_OR_SESSION_NOT_CHANGE:'App or session message have not changed !',
        SCRIPT_SUCCESS:'The script successfully !',
        ORDER_STATUS_NOT_SURE:'The order status is uncertain !',
        ORDER_NON_EXISTENT:'Order does not exist !'
    }

    @staticmethod
    def get_desc(result_code):
        return ResultCode.message_dict[result_code]