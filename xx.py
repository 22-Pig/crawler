def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.tbody.children:
        u = []  #学校信息
        col = 0
        for td in tr:
            temp = td.text.strip().strip("\n")  #取出td中的值
            col += 1
            if col == 2:  #对第二列进行处理，只取第一个数
                ls = temp.split()
                temp = ls[0]
            u.append(temp)
        ulist.append(u)