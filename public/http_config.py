#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import requests
from utils import read_config
from log import logger
#import json

RC= read_config.ReadConfig()


class Http_Config:

    def __init__(self):
        global scheme, host, port, timeout
        scheme = RC.get_http("protocol")
        host = RC.get_http("host")
        port = RC.get_http("port")
        timeout = RC.get_http("timeout")
        self.log = logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = scheme + '://' + host+ ':' + port
        return self.url

    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_files(self, filename):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = 'D:/test_frame/data/img/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    # defined http get method
    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except:
            self.log.error("Time out!")
            return None

    # defined http post method
    # include get params and post data
    # uninclude upload file
    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data,
                                     timeout=float(timeout))
            # response.raise_for_status()
            return response
        except:
            self.log.error("Time out!")
            return None

    # defined http post method
    # include upload file
    def post_with_file(self):
        """
        defined post method with file
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            return response
        except:
            self.log.error("Time out!")
            return None

    # defined http post method
    # for json
    def post_with_json(self):
        """
        defined post method with json
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except:
            self.log.error("Time out!")
            return None


if __name__ == "__main__":
   Http_Config()
