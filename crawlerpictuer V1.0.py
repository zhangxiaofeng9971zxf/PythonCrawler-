#爬照片最低端版本v1.0
import requests
url='http://imgsrc.baidu.com/forum/pic/item/9ccb855494eef01f9a7d953eedfe9925bd317da0.jpg'
try:
    kv = {'user-agent':'Mozilla/5.0'}#把爬虫伪装成一个浏览器
    r = requests.get(url,headers=kv)#爬取页面
    r.raise_for_status()#返回爬取结果 若是200 则爬成功。
    with open('p2.jpg','wb')as f: #爬下来的文件是二进制的，所以要把图片用二进制打开
        f.write(r.content)

    print('爬取成功')
except:
    print('爬取失败')