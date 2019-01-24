#根据IP138接口，来查询ip地址
import requests
url='http://m.ip138.com/ip.asp?ip='#ip138网站在查ip的接口
ip_search =input('请输入ip地址：类似8.8.8.8:')
try:
    kv = {'user-agent':'Mozilla/5.0'}#把爬虫伪装成一个浏览器
    r = requests.get(url+ip_search,headers=kv)#爬取页面
    r.raise_for_status()#返回爬取结果 若是200 则爬成功。
    r.encoding = r.apparent_encoding  # 把爬的结果编码模式换成可读的。
    print(r.text[-500:])
except:
    print('爬取失败')