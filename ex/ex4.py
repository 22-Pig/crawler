import requests
import os

url = "http://www.zwu.edu.cn/_upload/article/images/04/17/e8b3385c4fe5aa24a09339dde733/e1876272-63d4-4872-a7bb-be9b4a998cbd.jpg"
root = "E://Desktop//"
# 分离图片地址取最后字段
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
