#!/usr/bin/env python
#-*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib2
from bs4 import BeautifulSoup
import time
import pymysql
import function_urllist

url_list= function_urllist.newurl_list()
for url in url_list:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
    }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    count = soup.select('div.comment > h3 > span.comment-vote > span')
    users = soup.select('div.comment > h3 > span.comment-info > a')
    time = soup.select('div.comment > h3 > span.comment-info > span.comment-time')
    comments = soup.select('div.comment > p ')
# print data
# print soup
# print count
# print users
# print time


values_list= []
for index, item in enumerate(comments):
    temp = time[index].get_text().strip(),\
           users[index].get_text().strip(), \
           comments[index].get_text().strip(), \
           count[index].get_text().strip()
    values_list.append(temp)
print values_list



def execute(sql):
   with pymysql.connect(host='localhost', user='root', password='123456', db='douban_comment', port=3306, charset='utf8') as cur:
       cur.execute(sql)



def executemany(sql,args):
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='douban_comment', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.executemany(sql,args)
    conn.commit()
    conn.close()

execute('DROP TABLE IF EXISTS content;')
execute('CREATE TABLE IF NOT EXISTS content(id int not null primary key auto_increment, date date, \
user varchar(100), comment varchar(500), vote int(15));')

executemany('''insert into content (date,user,comment,vote) values(%s,%s,%s,%s)''', values_list)
