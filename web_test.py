# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: web_test.py
@time: 2018/12/10 下午10:15

这一行开始写关于本文件的说明与解释
"""

import requests

url = 'http://www.baidu.com'
url2 = 'http://39.107.252.164:8000'
res = requests.get(url2,timeout=5)
print("\n\nerr code",res.status_code)
print(res.content)