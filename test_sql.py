import requests

req = requests.get("http://127.0.0.1:8888/login?",params={'name':'xiaoming','pwd':'111'})
response = req.json()
print(response['code'])