# /usr/bin/env python
# -*- coding=utf-8 -*-
# --------------------
# 程序：抓取豆瓣某影评全部URL
# 版本：0.1
# 作者： amy
# 语言：python
# 功能：urlparse模块分割出参数，循环取参
# 日期：20170517
# ----------------------

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib2
from bs4 import BeautifulSoup
import time
import pymysql
import urlparse
import urllib



url = 'https://movie.douban.com/subject/26683290/comments?start=0&limit=20&sort=new_score&status=P'
result = urlparse.urlparse(url)
urlscheme = result.scheme
urlnetloc = result.netloc
urlpath = result.path
urlquery = result.query
t = urlparse.parse_qs(urlquery, True)
print result
#print t
print urlquery
#print t['start']
#u = urlparse.urlunparse(result)
#print u
#print t.get('start')
t['sort'] = 'new_score'
t['status'] = 'P'
t['limit'] = '20'

#t['start'] = [2]
#print t

#start数组
count = 0
start = 1
list_start = [start]
while count<5:
    start = start + 20
    list_start.append(start)
    count = count + 1
    print list_start

newurl_list=[]
for index,count in enumerate(list_start):
    t['start'] = list_start[index]
    newurlquery = urllib.urlencode(t)
    data = (urlscheme, urlnetloc, urlpath,'',newurlquery ,'')
    newurl = urlparse.urlunparse(data)
    print newurl
    newurl_list.append(newurl)
print newurl_list




#    print t
#    url_list = url_list.append(url)
#    print url_list





