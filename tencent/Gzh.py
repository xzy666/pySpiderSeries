# coding:utf-8

import bs4
import re
import requests
import sqlite3 as sqlite
import json


class Gzh(object):
    '''
        利用新的接口爬取微信公众号

        https://mp.weixin.qq.com/s/67sk-uKz9Ct4niT-f4u1KA 这篇文章介绍了为私信新开放的接口

        思路还是很简单 登录拿到cookie 搜索相关公众号的名字 拿到返回的fake_id 就能获取到相关的公众号的文章
        整体来说还是比较简单的
    '''

    cookie = '你的cookie'
    referer = 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&lang=zh_CN&token=1146682319'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    X_Requested_With = 'XMLHttpRequest'
    Accept = 'application/json, text/javascript, */*; q=0.01'
    Host = 'mp.weixin.qq.com'
    headers = {'User-Agent': user_agent, 'Referer': referer, 'Host': Host,
               'cookie': cookie, 'Accept': Accept}
    fake_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz'
    article_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
    con = sqlite.connect("./gzh.db")

    def __int__(self):
        self.con.execute(
            'CREATE TABLE Gzh_info(id INTEGER PRIMARY KEY AUTOINCREMENT,fakeid VARCHAR(50) UNIQUE NOT NULL ,alias VARCHAR(50),round_head_img TEXT,service_type INTEGER)')
        self.con.commit()

    def searchGzhByName(self, name):
        '''
            搜索名字 拿fake_id
        :param name: 公众号的名称
        :return:
        '''
        payload = {'token': '你的token', 'lang': 'zh_CN', 'f': 'json', 'ajax': 1, 'random': 0.6211676955829073,
                   'action': 'search_biz', 'begin': 0, 'count': 10, 'query': name}
        response = requests.get(url=self.fake_url, params=payload, headers=self.headers)
        result = json.loads(response.text)
        if result['base_resp']['ret'] == 0:
            for i in result['list']:
                sql = "insert into Gzh_info VALUES (xxxxxxxxxx)"
                self.con.execute(sql)
                self.con.commit()

    def getArticlesByFakeId(self, fake_id):
        '''
            根据fake_id来获取指定公众号下的文章
            默认是一次拿到5篇 可以自己指定 建议一次五条获取就好
        :param fake_id:
        :return:
        '''
        payload = {'token': '你的token', 'lang': 'zh_CN', 'f': 'json', 'ajax': 1, 'random': 0.6211676955829073,
                   'action': 'list_ex', 'begin': 0, 'count': 10, 'fakeid': fake_id, 'query': '', type: 9}
        response = requests.get(url=self.article_url, params=payload, headers=self.headers)
        result = json.loads(response.text)
        print result
        exit()  # 后面的就不继续往下写了 思路应该是很明朗的


G = Gzh()
G.searchGzhByName('easy')
