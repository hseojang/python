import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/emp'

response = requests.get(url)
html = response.text


print(html)
