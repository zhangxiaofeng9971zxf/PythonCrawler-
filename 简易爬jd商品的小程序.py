#怎么爬取一个jd页面的商品信息
import requests
url = 'https://item.jd.com/884953.html'
try:
    kv = {'user-agent':'Mozilla/5.0'}#把爬虫伪装成一个浏览器
    r = requests.get(url,headers=kv)#爬取页面
    r.raise_for_status()#返回爬取结果 若是200 则爬成功。
    r.encoding =r.apparent_encoding#把爬的结果编码模式换成可读的。
    print(r.text)
except:
    print('爬取失败')

