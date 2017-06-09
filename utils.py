#!/usr/bin/env python
# -*- coding=utf-8 -*-
import pymysql
import re
import config
import requests


def execute(sql, mysql_uri=config.MYSQL_URI, charset='utf8'):
    '''
    执行sql语句
    :param sql: 需要执行的sql语句
    :param mysql_uri: mysql的uri ex: mysql://root:123456@localhost:3306/douban_comment, 默认读取config.py中的MYSQL_URI
    :param charset: 数据库编码格式，默认为utf8
    :return: 执行的sql语句的结果
    '''
    user, password, host, port, db = re.compile(r'mysql://(\w*):(\w*)@(\w*):(\d*)/(\w*)').findall(mysql_uri)[0]
    with pymysql.connect(host=host, user=user, password=password, db='douban_comment', port=int(port), charset=charset) as cur:
        cur.execute(sql)
        return cur.fetchall()


class MyRequests(object):
    def __init__(self, headers=None, proxies=None):
        self.req = requests.Session()
        default_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
        }
        self.req.headers.update(default_header)
        if headers:
            self.req.headers.update(headers)
        if proxies:
            self.req.proxies.update(proxies)

    def get(self, **kwargs):
        return self.req.get(**kwargs)

    def post(self, **kwargs):
        return self.req.post(**kwargs)
