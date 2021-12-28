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
    for tr in soup.tbody.children:
        # 如果tr标签的类型不是bs4库中定义的tag类型，则过滤掉
        if isinstance(tr, bs4.element.Tag):
            # 将所有的a标签存为一个列表类型
            a = tr('a')
            # 将所有的td标签存为一个列表类型
            tds = tr('td')
            ulist.append(
                [tds[0].text.strip(), a[0].text.strip(), tds[4].text.strip()])


# 打印出ulist列表的信息，num表示希望将列表中的多少个元素打印出来
def printUnivList(ulist, num):
    # 0、1、2为槽,{3}表示若宽度不够,使用format的3号位置处的chr(12288)(中文空格)进行填充
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "大学名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


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
    url = 'https://www.shanghairanking.cn/rankings/bcur/2021'
    path = 'E://Desktop//univlist.txt'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # printUnivList(uinfo, 20)
    print(uinfo)
    # saveText(path, uinfo)


main()
