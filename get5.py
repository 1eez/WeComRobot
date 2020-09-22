# !/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################
#
#  爬虫程序5.0版本 - 将爬虫的数据，转换成推送需要的格式
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

    jsonData = json.loads(r.content)

    topics = jsonData['body']['datas']

    for topic in topics:
        result = re.findall(todayStr, topic['title'])

        if result:
            formatStr = ''
            groupList = topic['shareImageInfos']
            for group in groupList:
                formatStr = formatStr + group['title'] + '\n '
                newslist = group['content']
                for news in newslist:
                    formatStr = formatStr + '>' + news + '\n '
            print(formatStr)

else:
    print("error")
