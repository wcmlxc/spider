#!/usr/bin/env python
# -*- coding=utf-8 -*-
import business
import config

business.create_table()
next_page_url = business.get_current_comments(config.BASE_URL)

while (True):
    pass
