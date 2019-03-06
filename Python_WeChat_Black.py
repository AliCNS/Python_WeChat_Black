#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Author    : Ali
# Time      : 2019/3/4
# File      : Python_WeChat_Black.py
# Site      : https://ros.ac
# Mail      : ali@ros.ac
# Created by: PyCharm

import itchat
import time

# 扫码登录网页版微信
itchat.auto_login(True)
# 获取好友列表排除自己
friendList = itchat.get_friends(update=True)[1:]
print("总好友数:", len(friendList), "人。")
n = 0
# 遍历好友
for friend in friendList:
    n += 1
    print("正则测试第 %s/%s 位好友，昵称是：%s" % (n, len(friendList), friend['NickName']))
    # 发送微信服务器拒收的特殊字符。
    itchat.send("Python Auto Send! జ్ఞ ా", toUserName=friend['UserName'])
    # 这个延迟不能取消，消息发送太快容易被微信拒收 会被提示 "发送消息过于频繁，等待对方接受你的好友请求后再发。"
    time.sleep(3)
print(input()+"测试完毕 %s/%s" % (n, len(friendList))+" 测试结果请打开手机微信客户端查看！")

# 写的不好各位大佬勿喷。