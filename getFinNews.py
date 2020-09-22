# !/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################
#
#  爬虫程序7.0版本 - 正式版本，清理无用的print
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

WXurl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXX0078'
headers = {'content-type': "application/json"}

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
                formatStr = formatStr + '## **<font color=\"#BD286F\">' + group['title'] + '</font>** \n '
                newslist = group['content']
                for news in newslist:
                    formatStr = formatStr + ' ##### - ' + news + '\n '
                formatStr = formatStr + '\n '

            formatStr = formatStr + '----------------------------\n '
            formatStr = formatStr + '[如需了解更多，请点击此处](https://m.jinrongbaguanv.com/details/details.html?id='+ str(topic['id']) +')\n '
            formatStr = formatStr + '----------------------------\n '
            formatStr = formatStr + '<font color="comment">更多意见与建议，可企业微信：lordli</font> \n '
            formatStr = {
                        "msgtype": "markdown",
                        "markdown": {
                        "content": formatStr }
                    }

            response  = requests.post(WXurl, json = formatStr, headers = headers)

            if (response.status_code == 200):
                print ("已成功发送早报")

else:
    print("error")
