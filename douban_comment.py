#/usr/bin/env python
#-*- coding=utf-8 -*-
#--------------------
# 程序：爬豆瓣影评
# 版本：0.1
# 作者： amy
# 语言：python
# 功能：1.生成text.txt文件 2.写入数据库douban_comment
#日期：20170517
#----------------------

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib2
from bs4 import BeautifulSoup
import time
import pymysql

url = 'https://movie.douban.com/subject/26683290/comments'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
}
data = requests.get(url, headers = headers)
soup = BeautifulSoup(data.text, 'lxml')
count = soup.select('div.comment > h3 > span.comment-vote > span')
users = soup.select('div.comment > h3 > span.comment-info > a')
time = soup.select ('div.comment > h3 > span.comment-info > span.comment-time')
comments = soup.select('div.comment > p ' )



# f = open ('./text.txt', 'wb')
# #f.write(count[0].get_text()+'\n')
# for index,item in enumerate(comments):
#     print time[index].get_text().strip() + '\n' + users[index].get_text() + ':' + item.get_text().strip().strip('\n') + '\n'
#     f.write(time[index].get_text().strip() + '\n' +users[index].get_text() + ':' + item.get_text().strip().replace('\n', ' ') + '\n\n')
# f.close()


#结果写入数据库
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
user varchar(50), comment varchar(500), vote int(11));')

executemany('''insert into content (date,user,comment,vote) values(%s,%s,%s,%s)''', values_list)
