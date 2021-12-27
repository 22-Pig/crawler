import requests

keyword = 'python'

url = "https://www.baidu.com/s"

try:
    kv = {'wd': keyword}
    hd = {'User-Agent': 'Chrome/96.0.4664.110'}
    r = requests.get(url, headers=hd, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
