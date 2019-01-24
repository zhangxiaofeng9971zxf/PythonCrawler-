#从最好大学网爬取信息v1.0
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):#获取网页内容
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 把爬虫伪装成一个浏览器
        r = requests.get(url, headers=kv,timeout= 30)  # 爬取页面
        r.raise_for_status()  # 返回爬取结果 若是200 则爬成功。
        r.encoding= r.apparent_encoding
        return r.text
    except:
        return ''
def fillUniList(ulist,html):#页面信息放在列表
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:#所有信息在tbody标签下的tr标签下的td标签中
        if isinstance(tr,bs4.element.Tag):#isinstance(类，需要判断的东西)，也就是说要判断只有tr标签中的内容
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])#把所td标签中的内容输入
def printUniList(ulist,num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名','学校名称','分数'))#^表示居中 数字表示字符串长度
    for i in range(num):
        u = ulist[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))
def main():
    uninfo =[]
    url = input('请输入需要爬取页面的url：')
    #url ='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html#top'
    html = getHTMLText(url)
    fillUniList(uninfo,html)
    printUniList(uninfo,20)
main()