#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

from redis.sentinel import Sentinel
from config import config

sentinel = Sentinel([
     ('192.168.39.57',26379),
     ('192.168.39.110',26379),
     ],
    socket_timeout=0.5,
)

# 获取主服务器地址
master = sentinel.discover_master(config.REDIS['sentinel']['master'])
print(master)

# 获取从服务器地址
slave = sentinel.discover_slaves(config.REDIS['sentinel']['master'])
print(slave)

# 获取主服务器进行写入mq
def write_mq(theme, msg):

    master_write = sentinel.master_for(config.REDIS['sentinel']['master'],
                                       socket_timeout=0.5,
                                       password=config.REDIS['password'],
                                       db=config.REDIS['database']
                                       )

    return master_write.set(theme, msg)

# 获取从服务器进行读取
def read_mq(theme):

    slave_read = sentinel.slave_for(config.REDIS['sentinel']['master'],
                                    socket_timeout=0.5,
                                    password=config.REDIS['password'],
                                    db=config.REDIS['database']
                                    )

    return slave_read.get(theme)


if __name__=='__main__':
    write_mq('apdu','00A4000000')
    read_mq('apdu')