# !/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################
#
#  爬虫程序4.0版本 - 测试往企业微信群里发送消息
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

# 下行URL中的XXXX，可在企业微信申请机器人的时候，自动获得，替换就好
# &debug=1 的意思是如果过程报错的话，可以看到详细的错误信息，仅是过程需要，正式版可去掉

url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXX0078&debug=1'
body = {
        "msgtype": "markdown",
        "markdown": {
            "content": "lord测试。\n >lord测试。\n "
            }
        }
headers = {'content-type': "application/json"}

response  = requests.post(url, json = body, headers = headers)

# 返回结果信息，如果是错误的，则会返回具体的错误信息
print (response.text)
# 返回响应头，正确则为200
print (response.status_code)



