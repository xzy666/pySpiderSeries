# coding:utf-8
import requests
import re


# result = requests.get('http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1')
# print result.text


class TieBar_Scrawer(object):
    '''
        贴吧帖子爬取
    '''

    def __init__(self, url):
        self.url = url

    def getTitle(self):
        reg = re.compile(r'<h3 class="core_title_txt pull-left.*?" title="(.*?)" style="width: 396px">.*?</h3>',
                         re.DOTALL)
        re.findall(self.getRawText(), reg)

    def getRawText(self, page=1):
        result = requests.get(self.url % page)
        return result.text

    def getPageNum(self):
        reg = re.compile(
            r'<li class="l_reply_num".*?>.*?<span class="red" .*?>.*?</span>.*?<span class="red">(.*?)</span>.*?</li>',
            re.DOTALL)
        nums = re.findall(reg, self.getRawText())
        return nums[0]

    def getRealContent(self, page=1):
        reg = re.compile(r'<div id="post_content_.*?" class="d_post_content j_d_post_content ">(.*?)</div>', re.DOTALL)
        contents = re.findall(reg, self.getRawText())
        return contents

    def start(self):
        while True:
            print '请输入要查看的页面,按Q退出'
            page = raw_input()
            no = 1 + 30 * int(page)
            if page == 'Q':
                print 'Bye~'
                return
            if page < 1 or page > self.getPageNum():
                print 'num wrong~'
                continue
            for i in S.getRealContent(page):
                print '-----------------------------------------------------------------------------'
                print '第', no, '楼'
                no += 1
                print Tools().replace(i)


class Tools(object):
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


S = TieBar_Scrawer('http://tieba.baidu.com/p/3138733512?see_lz=1&pn=%d')
print '该帖子共', S.getPageNum(), '页'
print S.start()
