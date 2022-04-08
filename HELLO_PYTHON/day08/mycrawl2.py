import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/emp'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('tbody')
trs = tbody.select('tr')
print("아이디\t이름\t성별\t주소")
for tr in trs:
    e_id = tr.select('td')[0].text
    e_name = tr.select('td')[1].text
    sex = tr.select('td')[2].text
    addr = tr.select('td')[3].text
    print("{}\t{}\t{}\t{}".format(e_id, e_name, sex, addr))