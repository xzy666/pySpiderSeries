# coding:utf-8

import requests
import re
import codecs
import jieba
from wordcloud import WordCloud, STOPWORDS
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class Weibo(object):
    '''
        爬取某个明星的个人信息 词云做数据分析
        //例子是赵丽颖
    '''
    headers = {
        "Host": "m.weibo.cn",
        "Referer": "https://m.weibo.cn/",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) "
                      "Version/9.0 Mobile/13B143 Safari/601.1",
    }
    params = 'uid=1259110474&luicode=10000011&lfid=100103type = 1 & q = 赵丽颖&type=uid&value=1259110474&containerid=1076031259110474&page=%d'
    url = 'https://m.weibo.cn/api/container/getIndex?'

    def __init__(self):
        pass

    def getBasicInfo(self):
        result = requests.get(self.url + self.params % 1, headers=self.headers).json()
        return result.get('cardlistInfo')

    def getDetailedInfo(self, page):
        result = requests.get(self.url + self.params % page, headers=self.headers).json()
        return result.get('cards')

    def fecth_data(self):
        page = 1
        count = 0
        while page <= int(self.getBasicInfo().get('total')):
            blogs = DataDeal().clean_data(self.getDetailedInfo(page))
            count = len(blogs) + count
            print("抓取第{page}页，目前总共抓取了 {count} 条微博".format(page=page, count=count))
            page += 1
            with codecs.open('weibo1.txt', 'a', encoding='utf-8') as f:
                f.write("\n".join(blogs))
        print 'done!'
        exit()


class DataDeal(object):
    def clean_data(self, data):
        blogs = []
        for i in data:
            if i.get('card_type') == 9:
                dr = re.compile(r'</?\w+[^>]*>', re.S)
                text = re.sub(dr, '', i.get('mblog').get('text'))
                blogs.append(text)
        return blogs


def generate_image():
    data = []
    # jieba.analyse.set_stop_words("./weibo1.txt")

    with codecs.open("weibo1.txt", 'r', encoding="utf-8") as f:
        for text in f.readlines():
            data.extend(" ".join(jieba.cut(text, cut_all=True)))

        f = codecs.open(r'./weibo_jieba.txt', 'w', encoding='utf-8')
        f.write(''.join(data))
        f.close()

    #
    #     mask_img = plt.imread('test1.jpg')
    #     wordcloud = WordCloud(
    #         background_color='white',
    #         mask=mask_img
    #     ).generate(" ".join(data))
    #     plt.imshow(wordcloud.recolor(random_state=3),
    #                interpolation="bilinear")
    #     plt.axis('off')
    #     plt.savefig('./heart2.jpg', dpi=1600)

    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, 'weibo_jieba.txt')).read()

    # read the mask image
    # taken from
    # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
    alice_mask = np.array(Image.open(path.join(d, "test1.jpg")))

    stopwords = set(STOPWORDS)
    stopwords.add("said")
    wc = WordCloud(background_color="white",  # 设置背景颜色
                   mask=alice_mask,  # 设置背景图片
                   max_words=2000,  # 设置最大显示的字数
                   # stopwords = "", #设置停用词
                   font_path="FZHTJW.TTF",
                   # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
                   )
    #
    # wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
    #                stopwords=stopwords)
    # generate word cloud
    wc.generate_from_frequencies(text)

    # store to file
    wc.to_file(path.join(d, "alice.png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()


#
# W = Weibo()
# W.fecth_data()
generate_image()
# print u'\u8ba9'
