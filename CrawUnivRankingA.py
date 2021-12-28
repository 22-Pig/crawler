import bs4
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for table in soup.find_all('table'):
        for tr in table.tbody.tr.next_siblings:
            uu = []
            for index, item in enumerate(tr):
                if index == 3:
                    continue
                uu.append(item.text)
            ulist.append(uu)


def saveText(filename, data):
    file = open(filename, 'w')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '').replace('\'', '')
        s += '\n'  # 每行末尾追加换行符
        file.write(s)
    file.close()
    print("txt文件保存成功")


def main():
    uinfo = []
    url = 'http://www.gaosan.com/gaokao/196075.html'
    path = 'E://Desktop//univlist.txt'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # print(uinfo)
    saveText(path, uinfo)


main()
