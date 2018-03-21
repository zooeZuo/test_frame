#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

import redis
import os

sentinel_server = ['192.168.39.57:26379','192.168.39.110:26379']


def queue(host, port):
    strs = ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(16)))
    pool = redis.ConnectionPool(host=host, port=port, db=0)
    r = redis.Redis(connection_pool=pool)
    r.lpush('low_task_queue', strs)


def get_sentinel():
    global master_host
    global master_port

    for info in sentinel_server:
        host = info.split(':')[0]
        port = info.split(':')[1]
        try:
            r = redis.Redis(host=host, port=port)
            info = r.info('sentinel')['master0']['address'].split(':')
            master_host = info[0]
            master_port = info[1]
        except Exception as e:
            print('connect to sentinel error: %s' % e)
            pass
        else:
            break


if __name__ == "__main__":
    get_sentinel()
    while True:
        try:
            queue(master_host, master_port)
        except Exception as e:
            print('connect redis error %s' % e)
            get_sentinel()
            continue
