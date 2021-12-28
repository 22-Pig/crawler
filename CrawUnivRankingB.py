import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find('div', {'id': 'data196075'})
    for table in div.find_all('table'):
        tr = table.find('tr')
        for td in tr.next_siblings:
            # print(td.text)
            tds = td.text
        print(tds)
            # ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.gaosan.com/gaokao/196075.html'
    html = getHTMLText(url)
    # print(fillUnivList(uinfo, html))
    fillUnivList(uinfo, html)
    # print(uinfo)
    # printUnivList(uinfo, 20)


main()