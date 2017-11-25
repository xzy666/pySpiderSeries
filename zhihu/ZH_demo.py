# coding:utf-8

import requests
# import re
from bs4 import BeautifulSoup
import urllib
import json
import time
from pprint import pprint
import re


# from http import cookiejar


class ZhiHu(object):
    '''
        模拟知乎登录 和 爬取
        没有验证码：
            登录的时候 response头有一个z_c0 和原来的cookie凭拼接一下就是我们要的cookie
            z_c0如何获取呢？
            登录的时候response 头里面第三个set-cookie里面有
            正则匹配到z_c0
            然后就拿到要的cookie了

        补充：由于知乎限制的太多 对验证码如下操作
        获取验证码id 获取验证码  将XSRF PWD PHONE 验证码坐标 打包发送
    '''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    referer = 'https://www.zhihu.com/'
    origin = 'https://www.zhihu.com'
    host = 'www.zhihu.com'
    accept = 'application/json, text/plain, */*'
    ContentType = 'application/x-www-form-urlencoded;charset=UTF-8'
    cookie = '''q_c1=0a0455b353cd4f0186b62adf0c2495fc|1509193541000|1509193541000; d_c0="AEBCfSbQmAyPTnnQt2dv3xKHugW13Gd0HPA=|1509193542"; _zap=e84963cf-ab47-4d25-8c5b-d3c6c1cc0f01; _xsrf=f6111331-e700-4b67-9aef-758fe10f6ada; capsion_ticket="2|1:0|10:1510962491|14:capsion_ticket|44:Yjk2OTUzMDczNDIxNDlkNmE3OTMxZjNhMjUzOTE2YjI=|dfb476fb8af6e77fb04e309a9e3cacc9f1534b249cab6f1ad3490924a9b4783a"; l_cap_id="MDdkODZlYTc4N2M0NGVlN2E1ZTdkZjhhMWE4N2UwNGQ=|1510962906|046d4d4579f22246f2b8778b43579d3781cb77d3"; r_cap_id="ZDhlN2UwMTdjMmFhNDMzM2E0OWQ4YWIzNTIwODUxYjA=|1510962906|10365ced5a6b25e5c10d0e6220e7f48195289633"; cap_id="MGFhOGRkMWUwN2FiNGNiZWE1M2Q2NTA2ZDZjYmU1ZjA=|1510962906|cabbc22338d8254afab816555dcbe5b8eb6b0679"; __utma=51854390.269528696.1509847772.1510959839.1510961799.3; __utmb=51854390.0.10.1510961799; __utmc=51854390; __utmz=51854390.1510961799.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20170212=1^3=entry_date=20171028=1;'''
    z_c0 = '你的z_c0'
    # session = requests.session()
    # session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
    headers = {'User-Agent': user_agent, 'Referer': referer, 'Origin': origin, 'Host': host,
               'Content-Type': ContentType, 'cookie': cookie + z_c0, 'Accept': accept}
    url = 'https://www.zhihu.com/'
    loginUrlByPhone = 'https://www.zhihu.com/login/phone_num'
    # captchaImgUrl = 'https://www.zhihu.com/captcha.gif?r=%s&type=login&lang=cn'
    captcha_type = 'cn'

    # captcha = {"img_size": [200, 44], "input_points": [[28.5 * 2, 25], [28.5 * 5, 25]]}

    def __init__(self, **some):
        self.phone_num = some['phone_num']
        self.password = some['password']

    def getIndex(self):
        result = requests.get(self.url, headers=self.headers)
        return result

    def getXsrf(self):
        soup = BeautifulSoup(self.getIndex().text, "html.parser")
        xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
        return xsrf

    # def getCaptchaImg(self):
    #     urllib.urlretrieve(self.captchaImgUrl, 'captcha.gif')
    #     return '获取到验证码图，请输入图片倒立文字的排位'

    def isLogin(self):
        # 通过查看用户个人信息来判断是否已经登录
        url = "https://www.zhihu.com/settings/profile"
        response = self.session.get(url, headers=self.headers, allow_redirects=False)
        code = response.status_code
        if code == 200:
            return True
        else:
            return False

    def login(self):
        data = {
            '_xsrf': self.getXsrf(),
            'password': self.password,
            'captcha_type': 'cn',
            'phone_num': self.phone_num,
            # 'captcha': self.captcha,#self.getCaptchaImg //频繁登录要验证码
        }
        response = requests.Session().post(self.loginUrlByPhone, data=data, headers=self.headers)
        print response.text
        pa = re.compile(r'.*?(z_c0=.*?);.*?', re.DOTALL)
        print re.findall(pa, response.headers['Set-Cookie'])[0]  # 拿到z_c0

        # print response.json()['msg']
        # 保存cookies到本地
        # self.session.cookies.save()

    def getIndexPage(self):
        url = 'https://www.zhihu.com'
        response = requests.Session().get(url, headers=self.headers, allow_redirects=False)
        print response.request.headers
        print response.text

Z = ZhiHu(phone_num='你的账号', password='你的密码')
Z.getIndexPage()
# print u' \u767b\u5f55\u6210\u529f'
# exit()
print
# Z.login()  # Z.getCaptchaImg()
