# coding:utf-8
import requests
import re


class QS_Scrawer(object):
    '''
        糗事百科爬取
    '''
    domain = 'https://www.qiushibaike.com'
    url = 'https://www.qiushibaike.com/8hr/page/'  # 默认爬取的网页url
    reg = r'<div class="article block untagged mb15 typs_recent" id=.*?>.*?<div class="author clearfix">.*?<a href="(/users/.*?)".*?<img src="(.*?)" alt="(.*?)">.*?</a>.*?</div>.*?<a href="(/article/.*?)".*?>.*?<div class="content">.*?<span>\n+(.*?)\n+</span>.*?</div>.*?</a>\n*?(.*?)\n*?</div>'  # 正则
    regImg = r'<div class="thumb">.*?<a href="/article/.*?" target="_blank">.*?<img src="(.*?)".*?>.*?</a>'  # 配图正则
    page = 1

    def __init__(self, url='', reg='', regimg=''):
        self.url = url if url else QS_Scrawer.url
        self.reg = reg if reg else QS_Scrawer.reg
        self.regImg = regimg if regimg else QS_Scrawer.regImg
        self.enable = True

    def getPatterns(self):
        return [re.compile(self.reg, re.DOTALL), re.compile(self.regImg, re.DOTALL)]

    def getRawText(self):
        return requests.get(self.url + str(self.page)).text

    def getItems(self):
        return re.findall(self.getPatterns()[0], self.getRawText())

    def printful(self):
        for i in self.getItems():
            print '-------------------*****------------------'
            print "用户主页地址：", self.domain + i[0]
            print "用户头像地址：", "http:" + i[1]
            print "用户名称：", i[2]
            print "段子主页：", self.domain + i[3]
            print "段子内容:", i[4]
            # print i[5]
            if i[5]:
                haveImg = re.findall(self.getPatterns()[1], i[5])
                if haveImg:
                    print "段子图片地址：", "http:" + haveImg[0]
                else:
                    print "段子图片地址：", "无配图"
            else:
                print "段子图片地址：", "无配图"

    def start(self):
        print '开始爬取糗事百科...如果失败，请自行修改正则\n' \
              '按Enter查看下一页...按Q退出...'

        while self.enable:
            flag = raw_input()
            self.page += 1
            if flag == 'Q':
                self.enable = False
                print 'Bye~'
                return
            print '努力爬取中...'
            try:
                self.printful()
            except requests.exceptions.ConnectionError:
                print '网络有问题哦!'


QS_Scrawer().start()
