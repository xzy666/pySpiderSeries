# coding:utf-8
import requests
import re


class TBMM_scrawer(object):
    '''
        淘宝mm 信息爬取
    '''

    def __init__(self, url):
        self.url = url

    def getRawText(self, page=1):
        result = requests.get(self.url % page)
        return result.text

    def getContent(self, page=1):
        reg = re.compile(
            r'<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.DOTALL)
        return re.findall(reg, self.getRawText())

    def start(self):
        while True:
            print '请输入要查看的页面,按Q退出'
            page = raw_input()
            if page == 'Q':
                print 'Bye~'
                return
            for i in self.getContent(page):
                print '-----------------------------------------------------------------------------'
                print '主页','http:'+i[0]
                print '头像','http:'+i[1]
                print '姓名',i[2]
                print '年龄',i[3]
                print '城市',i[4]
T = TBMM_scrawer('https://mm.taobao.com/json/request_top_list.htm?page=%d')
T.start()
