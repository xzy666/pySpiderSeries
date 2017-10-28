# coding:utf-8

import requests
# import re
from bs4 import BeautifulSoup
import urllib


class ZhiHu(object):
    '''
        模拟知乎登录 和 爬取

        补充：由于知乎限制的太多 对验证码标志也做了加密  我不想爬了 大致思路：
        获取验证码id 获取验证码  将XSRF PWD PHONE 验证码坐标 打包发送
    '''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    referer = 'https://www.zhihu.com/'
    headers = {'User-Agent': user_agent, 'Referer': referer}
    url = 'https://www.zhihu.com/'
    loginUrlByPhone = 'https://www.zhihu.com/login/phone_num'
    loginUrlByEmail = 'https://www.zhihu.com/login/email'
    captchaImgUrl = 'https://www.zhihu.com/captcha.gif?r=%s&type=login&lang=cn'
    captcha_type = 'cn'
    captcha = {"img_size": [200, 44], "input_points": [[28.5*2, 25], [28.5*5, 25]]}

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

    def getCaptchaImg(self):
        urllib.urlretrieve(self.captchaImgUrl, 'captcha.gif')
        return '获取到验证码图，请输入图片倒立文字的排位'

    def login(self):
        data = {
            '_xsrf': self.getXsrf(),
            'password': self.password,
            'captcha_type': self.captcha_type,
            'phone_num': self.phone_num,
            'captcha': self.captcha,
        }
        result = requests.post(self.loginUrlByPhone, data=data, headers=self.headers)

        return result.text


Z = ZhiHu(phone_num='xxxxx', password='xxxx')
print Z.login()
# Z.getCaptchaImg()
