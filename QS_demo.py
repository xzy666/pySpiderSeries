# coding:utf-8

import urllib2
import urllib

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
refer = 'https://pos.baidu.com/wcom?rdid=3007983&dc=3&di=u3007983&dri=0&dis=3&dai=1&ps=0x0&dcb=___adblockplus&dtm=HTML_POST&dvi=0.0&dci=-1&dpt=none&tsr=0&ti=%E5%A4%AE%E8%A7%86%E7%BD%91_%E4%B8%96%E7%95%8C%E5%B0%B1%E5%9C%A8%E7%9C%BC%E5%89%8D&ari=2&dbv=0&drs=1&pcs=300x250&pss=300x250&cfv=0&cpl=1&chi=2&cce=true&cec=UTF-8&tlm=1494577607&prot=2&rw=320&ltu=https%3A%2F%2Fstatic01.5plus.cntv.cn%2Fcntv%2Fsports%2Fnews%2Fchannel.html%3Fuid%3Du3007983%26width%3D300%26height%3D250%26at%3D3%26rsi0%3D300%26rsi1%3D250%26pat%3D17%26tn%3DbaiduCustNativeAD%26rss1%3D%2523FFFFFF%26conBW%3D1%26adp%3D1%26ptt%3D0%26titFF%3D%25E5%25BE%25AE%25E8%25BD%25AF%25E9%259B%2585%25E9%25BB%2591%26titFS%3D14%26rss2%3D%2523000000%26titSU%3D0&liu=https%3A%2F%2Fstatic01.5plus.cntv.cn%2Fcntv%2Fsports%2Fnews%2Frender.html%3Fuid%3Du3007983%26width%3D300%26height%3D250%26at%3D3%26rsi0%3D300%26rsi1%3D250%26pat%3D17%26tn%3DbaiduCustNativeAD%26rss1%3D%2523FFFFFF%26conBW%3D1%26adp%3D1%26ptt%3D0%26titFF%3D%25E5%25BE%25AE%25E8%25BD%25AF%25E9%259B%2585%25E9%25BB%2591%26titFS%3D14%26rss2%3D%2523000000%26titSU%3D0&ltr=https%3A%2F%2Fstatic01.5plus.cntv.cn%2Fcntv%2Fsports%2Fnews%2Fchannel.html%3Fuid%3Du3007983%26width%3D300%26height%3D250%26at%3D3%26rsi0%3D300%26rsi1%3D250%26pat%3D17%26tn%3DbaiduCustNativeAD%26rss1%3D%2523FFFFFF%26conBW%3D1%26adp%3D1%26ptt%3D0%26titFF%3D%25E5%25BE%25AE%25E8%25BD%25AF%25E9%259B%2585&ecd=1&uc=1680x947&pis=300x250&sr=1680x1050&tcn=1507820555&qn=bdba6e1dd2d01a19&tt=1507820555381.47.91.96'
cookies = 'CPROID=506B85F942A834D8A518F347A0269951:FG=1'
headers = {'User-Agent': user_agent, 'Referer': refer, 'Cookie': cookies}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason
