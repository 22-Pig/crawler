import requests
import os
from bs4 import BeautifulSoup

r = requests.get('http://www.zwu.edu.cn/24/list.htm')
r.raise_for_status
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

table = 0
for i in soup.descendants:
    if str(i.name).lower() == 'table':
        table = i

lst = []
for i in table.descendants:
    if str(i.name).lower() == 'img':
        if str(i.attrs['src']).count("/empty.gif") >= 1:
            continue
        lst.append('http://www.zwu.edu.cn/' + i.parent.attrs['href'])
# print(lst)

root = "E://Desktop//test//"
for i in range(len(lst)):
    path = root + str(i) + '.jpg'
    try:
        if not os.path.exists(path):
            r = requests.get(lst[i])
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("序号" + str(i) + "图片保存成功")
        else:
            print("序号" + str(i) + "文件已存在")
    except:
        print("序号" + str(i) + "图片爬取失败")
