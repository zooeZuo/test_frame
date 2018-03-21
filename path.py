#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import os

BaseDir = os.path.split(os.path.realpath(__file__))[0]
ConfigPath = os.path.join(BaseDir,'config','base_config.ini')
LOG_PATH = os.path.join(BaseDir,'log')
REPORT_PATH = os.path.join(BaseDir,'report')


if __name__=='__main__':
    print BaseDir
    print ConfigPath
    print LOG_PATH
    print REPORT_PATH