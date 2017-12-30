# -*- coding:utf-8 -*-
# Python3
# File    : hackjump
# Time    : 2017/12/30 22:44
# Author  : 知乎大佬@麦文俊

import base64
import json
from pprint import pprint

import requests
from Crypto.Cipher import AES

action_data = {
    "score": 999, # 游戏分数
    "times": 233, # 游戏时间
    "game_data": "{}" # 空
}

# 抓包，取wxgame_init里自己的session_id
session_id = "3rbIfrDpPVILOBtgSgC6uv4rHCsX92FLHX4BVOXzOqNFSKZFZiFBeNchdUX4hLTz2M0qbzpUpQ06PcvCwRIo8JNYS9MPBNRGcyM7PL+xUYdzAX1LO25dFTwhPbmVBOvQLHA66DpFq5d1EJaBPonjUw\u003d\u003d"

aes_key = session_id[0:16]
aes_iv = aes_key

cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)
str_action_data = json.dumps(action_data).encode("utf-8")

# pkcs#7填充
length = 16 - (len(str_action_data) % 16)
str_action_data += bytes([length]) * length
cipher_action_data = base64.b64encode(cryptor.encrypt(str_action_data)).decode("utf-8")  # 加密后的action_data

post_data = {
    "base_req": {
        "session_id": session_id,
        "fast": 1,
    },
    "action_data": cipher_action_data
}

# 无效的话，修改成抓包后自己的header
headers = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx7c8d593b2c3a7703/3/page-frame.html",
    "content-type": "application/json",
    "User-Agent": "MicroMessenger/6.6.1.1220(0x26060133) NetType/WIFI Language/zh_CN",
    "Content-Length": "0",
    "Host": "mp.weixin.qq.com",
    "Connection": "Keep-Alive"
}

url = "https://mp.weixin.qq.com/wxagame/wxagame_settlement"

response = requests.post(url, json=post_data, headers=headers)
pprint(response.json())


