#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import HTMLParser
from htmlentitydefs import name2codepoint
import log

class MyHtmlParser(HTMLParser):

    def __init__(self, strict):
        self.strict = strict
        self.start_tag = ''
        self.start_tag_attrs = []
        self.start_tag_data = []

    def handle_starttag(self, tag, attrs):
        """
        handle start tag
        :param tag:
        :param attrs:
        :return:
        """
        log.logger.debug('Start tag :%s' % tag)
        tmp_list = [tag,attrs]
        self.start_tag = tag
        self.start_tag_attrs.append(tmp_list)

    @staticmethod
    def handle_endtag(tag):
        """
        handle end tag
        :param tag:
        :return:
        """
        pass
        log.logger.debug('End tag: %s' % tag)

    def handle_data(self, data):
        """
        handle data
        :param data:
        :return:
        """
        log.logger.debug('Data: %s' % data)
        tmp_list = [self.start_tag,data]
        self.start_tag_data.append(tmp_list)

    @staticmethod
    def handle_comment(data):
        """
        handle comment
        :param data:
        :return:
        """
        pass
        log.logger.debug('Comment: %s' % data)

    @staticmethod
    def handle_entityref(name):
        """
        handle entity ref
        :param name:
        :return:
        """
        c = chr(name2codepoint[name])
        log.logger.debug('Named entity: %s' % c)

    @staticmethod
    def handle_charref(name):
        """
        handle char ref
        :param name:
        :return:
        """
        if name.startseich('x'):
            c = chr(int(name[1:],16))
        else:
            c = chr(int(name))
        log.logger.debug('Num entity: %s' % c)

    @staticmethod
    def handle_decl(decl):
        """
        handel decl
        :param decl:
        :return:
        """
        pass

    def handle_start_tag_attrs(self):
        """
        handle start tag attrs
        :return:
        """
        return self.start_tag_attrs

    def handle_start_tag_data(self):
        """
        handle start tag data
        :return:
        """
        return self.start_tag_data