import requests
from bs4 import BeautifulSoup

r = requests.get('http://python123.io/ws/demo.html')
r.raise_for_status
demo = r.text
# print(demo)

soup = BeautifulSoup(demo, 'html.parser')
# print(soup.p)
# print(soup.prettify())
for i in soup.html.descendants:
    print(i.name)
