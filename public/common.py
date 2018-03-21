#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

import json
import os
from xml.etree import ElementTree as ET

from xlrd import open_workbook

import http_config
from utils import read_config

localReadConfig = read_config.ReadConfig
BasePath = read_config.BaseDir
localHttpConfig = http_config.Http_Config

case_no = 0


def get_value_from_return_json(jsons, value1, value2):
    """
    get value by key
    :param jsons:
    :param value1:
    :param value2:
    :return:
    """
    info = jsons['info']
    group = info[value1]
    value = group[value2]
    return value


def show_return_msg(res):
    """
    show msg detail
    :param res:
    :return:
    """
    url = res.url
    msg = res.text
    print('\nRequest URL: ' + url)
    print('\nRequest Return Value: ' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=2))


# --------------------------Read TestCases Excel---------------------------------
def get_xls(xls_name, sheet_name):
    """
    get test data from xls file
    :param xls_name:
    :param sheet_name:
    :return:
    """
    cls = []

    xls_path = os.path.join(BasePath, 'data', xls_name)

    files = open_workbook(xls_path)

    sheet = files.sheet_by_name(sheet_name)

    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


# --------------------------Read SQL xml---------------------------

database = {}


def set_xml():
    """
    set sql xml
    :return:
    """
    if len(database) == 0:
        sql_path = os.path.join(BasePath, 'data', 'SQL.xml')
        tree = ET.parse(sql_path)
        for db in tree.findall('database'):
            db_name = db.get('name')

            table = {}
            for tb in db.getchildren():
                table_name = tb.get('name')

                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get('id')

                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table


def get_xml_dict(database_name, table_name):
    """
    get db by given name
    :param table_name:
    :param database_name:
    :return:
    """
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict


def get_sql(database_name, table_name, sql_id):
    """
    get sql by given name and sql_id
    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    """
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql


# -----------------------read APIUrl xml-----------------------

def get_url_from_xml(name):
    """
    get url from API_Url.xml by name
    :param name:
    :return:
    """
    url_list = []
    url_path = os.path.join(BasePath, 'data', 'API_Url.xml')
    tree = ET.parse(url_path)
    for u in tree.findall('url'):
        url_name = u.get('name')
        if url_name == name:
            for c in u.getchildren():
                url_list.append(c.text)

    url = '/'.join(url_list)
    return url


if __name__ == '__main__':
    # print(get_url_from_xml('PutApduScripts'))
    print(get_sql('test', 'mi_ap', '3'))
    print(get_url_from_xml('GPL'))
