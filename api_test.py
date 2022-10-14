import requests
import json
response_API = requests.get('http://127.0.0.1:8000/api/list/?format=json')

data = response_API.text
print(data)