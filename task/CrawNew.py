import requests
import os
from bs4 import BeautifulSoup
# pip install html-table
from HTMLTable import HTMLTable


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


# 获取目录信息
def getContent(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find('div', {'id': 'wp_news_w2'})
    for tbody in div.find_all('tbody'):
        uu = []
        a = tbody.select('a')

        title = a[0].attrs['title']
        uu.append(title)

        hrefPart = a[0].attrs['href']
        href = 'http://www.njupt.edu.cn/' + hrefPart
        uu.append(href)

        date = tbody.select('div')
        uu.append(date[0].text)

        # 获取新闻详细内容
        count = 0
        source = str()
        uu.extend(list(getDetail(href, count, source)))

        ulist.append(uu)
    return ulist


def getDetail(href, count, source):
    html = getHTMLText(href)
    soup = BeautifulSoup(html, "html.parser")
    info = soup.find('span', {'class': 'infoStyle'})
    count = info.select('span')[3]
    source = info.select('span')[4]
    source = source.text.replace('\n', '')
    return count.text, source


def createTable(uinfo):
    # 标题
    table = HTMLTable(caption='新闻汇总表')
    # 表头行
    table.append_header_rows((('新闻标题', '链接网址', '发布日期', '浏览次数', '文章来源'),))
    # 数据行
    table.append_data_rows(uinfo)
    # 标题样式
    table.caption.set_style({
        'font-size': '30px',
    })
    # 表格样式，即<table>标签样式
    table.set_style({
        'border-collapse': 'collapse',
        'word-break': 'keep-all',
        'white-space': 'nowrap',
        'font-size': '14px',
    })
    # 统一设置所有单元格样式，<td>或<th>
    table.set_cell_style({
        'border-color': '#000',
        'border-width': '1px',
        'border-style': 'solid',
        'padding': '5px',
        # 'min-width': '100px',
        'text-align': 'center'
    })
    # 表头样式
    table.set_header_row_style({
        'color': '#fff',
        'background-color': '#CCE8CF',
        'font-size': '18px',
    })
    # 覆盖表头单元格字体样式
    table.set_header_cell_style({
        'padding': '15px',
    })
    html = table.to_html()
    return html


def saveHtml(path, table):
    if not os.path.exists(path):
        os.mkdir(path)
    filename = path + 'res.html'
    with open(filename, 'w') as f:
        f.write(table)
        f.close()
    return 'success'


def main():
    uinfo = []
    path = 'C://temp//'
    for i in range(1, 8):
        url = 'https://www.njupt.edu.cn/53/list' + str(i) + '.psp'
        html = getHTMLText(url)
        getContent(uinfo, html)
    table = createTable(uinfo)
    print(saveHtml(path, table))


main()
