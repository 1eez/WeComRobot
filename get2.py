# !/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################
#
#  爬虫程序2.0版本 - 从文件中读取并解析json数据，提取需要的字段
#
#  @Author: lordli
#
#  @Date: 2020-09-17
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

    with open ('news.json', 'wb') as f:
        f.write(r.content)

    with open('news.json', 'r') as f:
        data1 = json.load(f)

    topics = data1['body']['datas']

    for topic in topics:
        result = re.findall(todayStr, topic['title'])

        if result:
           print (topic['shareImageInfos'])

else:
    print("error")

