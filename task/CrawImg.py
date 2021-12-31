import requests
import re
import os


# 获取网页数据
def getHTMLText(url):
    try:
        hd = {'User-Agent': 'Chrome/96.0.4664.110'}
        r = requests.get(url, headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "getHTMLText is Error"


def getImg(lst, html):

    # 解析下载好的网页，提取图片信息
    imageList = re.findall(r'/_upload/article.*?jpg', html)
    sifter = list(set(imageList))
    sifter.sort(key=imageList.index)

    for i in sifter:
        lst.append("http://www.njupt.edu.cn" + i)
    return lst


def saveImg(path, data):
    for i in range(len(data)):
        filename = path + str(i + 1) + '.jpg'
        # print(filename)
        if not os.path.exists(path):
            os.mkdir(path)
        try:
            r = requests.get(data[i])
            with open(filename, 'wb') as f:
                f.write(r.content)
                f.close()
        except:
            return 'error'
    return 'success'


def main():
    url = 'http://www.njupt.edu.cn/19/list.htm'
    uinfo = []
    path = 'C://TEMP//'

    html = getHTMLText(url)
    getImg(uinfo, html)
    print(saveImg(path, uinfo))


main()