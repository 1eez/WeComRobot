# !/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################
#
#  爬虫程序3.0版本 - 无需存储本地文件，格式化数据
#
#  @Author: lordli
#
#  @Date: 2020-09-21
#
#  @Python version: 3.7.7
#
#  @Libary: pip install requests
#
###########################################

import time
import requests
import json
import re

todayStr = str(time.localtime().tm_mon) + "月" + str(time.localtime().tm_mday) + "日"

url = "https://www.jinrongbaguanv.com/jinba/index_articles/1"
print("开始分析今天是否有早报")

r=requests.get(url)

if (r.status_code == 200):

    jsonData = json.loads(r.content) # 由于不再从文件中读取数据，这里要把json.load改成json.loads

    topics = jsonData['body']['datas']

    for topic in topics:
        result = re.findall(todayStr, topic['title'])

        if result:
           print (topic['shareImageInfos'])

else:
    print("error")

