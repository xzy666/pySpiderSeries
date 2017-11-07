# coding:utf-8
import requests
import _LWPCookieJar


class ZhiHu(object):
    '''
        人工登录 拿到cookies
        爬取知乎首页
    '''

    def __init__(self):
        self._session = requests.session()
        self._session.verify = False
        self._session.headers = {"Host": "www.zhihu.com",
                                 "Referer": "https://www.zhihu.com/",
                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36'
                                               ' (KHTML, like Gecko) Chrome/56.0.2924.87',
                                 }
        self._session.cookies = LWPCookieJar(filename=cookie_filename)
        try:
            self._session.cookies.load(ignore_discard=True)
        except:
            pass

    @need_login
    def send_message(self, user_id, content):
        """
        给指定的用户发私信
        :param user_id: 用户ID
        :param content: 私信内容
        """
        data = {"type": "common", "content": content, "receiver_hash": user_id}
        response = self._session.post(URL.message(), json=data)
        data = response.json()
        if data.get("error"):
            self.logger.info("私信发送失败, %s" % data.get("error").get("message"))
        else:
            self.logger.info("发送成功")
        return data

if __name__ == '__main__':
    zhihu=ZhiHu()
    profile = zhihu.user("xiaoxiaodouzi")
    _id = profile.get("id")
    zhihu.send_message(_id, "你好,这是来自Python之禅的问候")