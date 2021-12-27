import requests

hd = {'User-Agent': 'Chrome/96.0.4664.110'}

url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url, headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[0:1000])
except:
    print("爬取失败")
