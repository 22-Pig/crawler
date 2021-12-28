import requests
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
for i in table.descendants:
    if str(i.name).lower() == 'img':
        if str(i.attrs['src']).count("/empty.gif")>=1:
            continue
        print('http://www.zwu.edu.cn/'+i.parent.attrs['href'])