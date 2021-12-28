import requests

# r = requests.head('https://httpbin.org/get')
r = requests.get('https://httpbin.org/get')
print(r.headers)
print(r.text)
