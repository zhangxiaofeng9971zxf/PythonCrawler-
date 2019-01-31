#从妹子图网上爬照片的爬虫v1.0

import requests
from bs4 import BeautifulSoup
import time
def download_page(url):
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
   r = requests.get(url, headers=headers)
   r.encoding = 'gb2312'
   return r.text
def get_pic(pic_link):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(pic_link, headers=headers)  # 下载图片，之后保存到文件
    with open('pic{}'.format(pic_link.split('/')[-1]), 'wb') as f:
           f.write(r.content)
           time.sleep(0.1)


url ='http://www.meizitu.com/a/5557.html'
html=download_page(url)
soup = BeautifulSoup(html, 'html.parser')
pic_list = soup.find('div',class_="postContent").find_all('img')#在dic 这个标签下 找到img标签
for i in pic_list:
    pic_link = i.get('src')#在img标签中获取src后的值
    get_pic(pic_link)


