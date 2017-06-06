#!/usr/bin/env python
#-*- coding = utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import urllib2
import time
import urlparse
import urllib

url = 'https://movie.douban.com/subject/26683290/comments?start=0&limit=20&sort=new_score&status=P'
#headers = {
 #   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
#}
#data = requests.get(url, headers = headers)
#soup = BeautifulSoup(data.text, 'lxml')
#count = soup.select('div.comment > h3 > span.comment-vote > span')
#users = soup.select('div.comment > h3 > span.comment-info > a')
#time = soup.select ('div.comment > h3 > span.comment-info > span.comment-time')
#comments = soup.select('div.comment > p ' )

result = urlparse.urlparse(url)
urlscheme = result.scheme
urlnetloc = result.netloc
urlpath = result.path
urlquery = result.query
t = urlparse.parse_qs(urlquery, True)

t['sort'] = 'new_score'
t['status'] = 'P'
t['limit'] = '20'

#t['start'] = [2]
#print t

num = 0
start = 1
list_start = [start]
while num<20:
    start = start + 20
    list_start.append(start)
    num = num + 1
#    print list_start

def newurl_list():
    newurl_list=[]
    for index,num in enumerate(list_start):
        t['start'] = list_start[index]
        newurlquery = urllib.urlencode(t)
        data = (urlscheme, urlnetloc, urlpath,'',newurlquery ,'')
        newurl = urlparse.urlunparse(data)
#        print newurl
        newurl_list.append(newurl)
#    print newurl_list
    return newurl_list

list = newurl_list()
print list

