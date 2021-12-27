import requests

url = "https://m.ip138.com/iplookup.asp?ip="

try:
    hd = {'User-Agent': 'Chrome/96.0.4664.110'}
    r = requests.get(url + '218.75.41.141', headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
