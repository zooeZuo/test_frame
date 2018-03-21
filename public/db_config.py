#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import MySQLdb
from utils.read_config import ReadConfig
from log import logger

RC = ReadConfig()

class MySqlDB:

    global host, user, passwd, port, db, charset, config
    host = str(RC.get_db('host'))
    port = int(RC.get_db('port'))
    user = RC.get_db('user')
    passwd = RC.get_db('passwd')
    db = RC.get_db('db')
    charset = RC.get_db('charset')
    config = {
        'host': host,
        'port': port,
        'user': user,
        'passwd': passwd,
        'db': db,
        'charset': charset
    }

    def __init__(self):
        self.conn = None
        self.cur = None
        self.log = logger

    def connect_db(self,sqls):
        """
        connect database
        :param sqls:
        :return:
        """
        try:
            conn = MySQLdb.connect(**config)
            self.cur = conn.cursor()
            self.conn = conn
            self.log.debug('db connect successful !!!')
            return self.cur.execute(sqls)
        except Exception as e:
            self.log.error(str(e))

    def get_all(self):
        """
        get all results after execute sql
        :return:
        """
        try:
            value = self.cur.fetchall()
            return value
        except Exception as e:
            logger.error('数据库查询失败：%s' % e)

    def get_one(self):
        """
        get one results after execute sql
        :return:
        """
        try:
            value = self.cur.fetchone()
            return value
        except Exception as e:
            logger.error('数据查询失败：%s' % e)

    def close_db(self):
        """
        close database
        :return:
        """
        self.cur.close()
        self.conn.commit()
        self.conn.close()
        self.log.debug('db closed !!!')




if __name__ == '__main__':
    db = MySqlDB()
    sql = 'select * from mi_ap where test_id=1'
    ex = db.connect_db(sql)
    tem = db.get_one()
    print(tem)
    re_dict = dict()
    re_dict1 = tem[1]
    re_dict2 = tem[2]
    re_dict3 = tem[3]
    print(re_dict1)
    print(re_dict2)
    print(re_dict3)

    db.close_db()
