#!/usr/bin/env python
# -*- coding=utf-8 -*-
import utils
import config
from bs4 import BeautifulSoup


def create_table():
    '''
    创建content表格，如果存在的话先drop
    :return: 创建成功返回True，否则返回Fasle
    '''
    try:
        utils.execute('DROP TABLE IF EXISTS content')
        utils.execute('''CREATE TABLE IF NOT EXISTS content (
                    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    date DATE,
                    user VARCHAR(100),
                    comment VARCHAR(500),
                    vote INT(15));''')
        return True
    except Exception, e:
        print e
        return False


def get_current_comments(url):
    req = utils.MyRequests()
    data = req.get(url=url)
    soup = BeautifulSoup(data.text, 'lxml')
    comments_item = soup.select('div.comment-item')
    for index, item in enumerate(comments_item):
        print('**********{}**********'.format(index))
        vote = item.find("span", class_="votes").string.strip()
        username = item.select('span.comment-info > a')[0].string.strip()
        comment_time = item.find("span", class_="comment-time").string.strip()
        comment_content = item.select('div.comment > p')[0].string.strip()
        print vote, username, comment_time, comment_content
        # break
    # vote = soup.select('div.comment > h3 > span.comment-vote > span')
    # print vote
    next_page_url = soup.find("a", class_="next")['href']
    if next_page_url:
        return get_current_comments("" + next_page_url)
    else:
        return


get_current_comments(config.BASE_URL)
