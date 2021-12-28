import requests

payload = dict(userName='2021037154', passWord='123123')
r = requests.post('https://httpbin.org/post', data=payload)
# r = requests.get('http://localhost:8080/page/login.html', data=payload)
print(r.text)
