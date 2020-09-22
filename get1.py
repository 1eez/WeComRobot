# !/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################
#
#  爬虫程序1.0版本 - 读取到html请求后的json数据，并保存到本地
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

import time  # 引入time模块，获取当前日期
import requests # 引入爬虫模块，获取json数据

currentdate = time.strftime("%Y-%m-%d", time.localtime())
print ("当前日期：" + str(currentdate))

url = "https://www.jinrongbaguanv.com/jinba/index_articles/1"
print("开始分析今天是否有早报")

r=requests.get(url)

if (r.status_code == 200):
    print(r.content)

    with open ('news.json', 'wb') as f:
        f.write(r.content)

else:
    print("error")

