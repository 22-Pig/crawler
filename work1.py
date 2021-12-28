import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.zwu.edu.cn/24/list.htm')
r.raise_for_status
r.encoding = r.apparent_encoding
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')
# print(soup.p)
# print(soup.prettify())
for i in soup.li.next_siblings:
    # print(type(i))
    if str(type(i)) == "<class 'bs4.element.Tag'>":
        print(i.text.replace("\n", ""))
        href = i.a.attrs['href']
        if href.count("://") >= 1:
            print(href)
        elif href[0:1] == "/":
            print("http://www.zwu.edu.cn" + href)
        else:
            print("http://www.zwu.edu.cn/24/" + href)
