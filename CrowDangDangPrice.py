import bs4
import requests
import re
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find('div', {'name': 'm940032_pid0_t12840'})
    for li in div.find_all('li'):
        # print(li.text)
        uu = []
        a = li.find('a')
        uu.append(a.attrs['title'].strip())
        price1 = li.find('span', {'class': 'search_now_price'})
        uu.append(price1.text)
        price2 = li.find('span', {'class': 'search_pre_price'})
        uu.append(price2.text)
        for publsh in li.select("[class='search_book_author']"):
            author = publsh.select("a")[0].get('title')
            date = publsh.select('span')[1]
            cbs = publsh.select('span')[2]
            uu.append(author)
            uu.append(date.get_text().strip().replace('/', ''))
            uu.append(cbs.get_text().strip().replace('/', ''))
        # print(uu)
        ulist.append(uu)


def saveText(filename, data):
    file = open(filename, 'w', encoding='utf-8')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '').replace('\'', '')
        s += '\n'  # 每行末尾追加换行符
        file.write(s)
    file.close()
    print("文件保存成功")


def main():
    # goods = '程序设计'
    # depth = 3
    # start_url = 'http://search.dangdang.com/?key=' + goods
    # infoList = []
    # for i in range(depth):
    #     try:
    #         url = start_url + '&s=' + str(44 * i)
    #         html = getHTMLText(url)
    #         parsePage(infoList, html)
    #     except:
    #         continue
    # printGoodsList(infoList)
    uinfo = []
    url = 'http://search.dangdang.com/?key=%B3%CC%D0%F2%C9%E8%BC%C6&act=input'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    path = 'E://Desktop//dangdang.csv'
    saveText(path, uinfo)


main()