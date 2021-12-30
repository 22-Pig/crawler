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


def fillBookList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
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
    uinfo = []
    for i in range(1, 4):
        url = 'http://search.dangdang.com/?key=%B3%CC%D0%F2%C9%E8%BC%C6&act=input&page_index=' + str(
            i)
        html = getHTMLText(url)
        fillBookList(uinfo, html)
    # print(uinfo)
    path = 'E://Desktop//dangdang.txt'
    saveText(path, uinfo)


main()