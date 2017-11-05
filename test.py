# coding:utf-8
import requests

url = 'https://m.weibo.cn/api/container/getIndex?uid=3952070245&luicode=10000011&lfid=100103type%3D1%26q%3D%E8%8C%83%E5%86%B0%E5%86%B0&type=uid&value=3952070245&containerid=1076033952070245'
headers = {
    "Host": "m.weibo.cn",
    "Referer": "https://m.weibo.cn/u/3952070245",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) "
                  "Version/9.0 Mobile/13B143 Safari/601.1",
}

result = requests.get(url, headers=headers)
cards = result.json().get('cards')
for card in cards:
            # 每条微博的正文内容
            if card.get("card_type") == 9:
                text = card.get("mblog").get("text")
                print text
                exit()
