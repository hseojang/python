import requests
from bs4 import BeautifulSoup

url = 'https://vip.mk.co.kr/newSt/rate/item_all.php'

response = requests.get(url)
response.encoding = 'utf-8' 
page = response.text

soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
table = soup.select_one('table', {'border':'0', 'cellspacing':'0', 'cellpadding':'0'})
listtd = table.select('td', {'width':'215', 'align':'center', 'valign':'top'})
print(listtd)
print("종목명\t현재가\t등락폭")

# for tr in trs:
#     print(tr.text)
    
    #
    # if tr.select('td')[0] == tr.select('td', {'colspan':'3'}):
    #     print("종목분류 : {}".format(tr.select('td').text))
    # s_name = tr.select('td')[0].text
    # s_price = tr.select('td')[1].text
    # s_updown = tr.select('td')[2].text
    # print("{}\t{}\t{}".format(s_name, s_price, s_updown))
    #



