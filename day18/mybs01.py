import requests
from bs4 import BeautifulSoup
import datetime
from day18.DaoStock import DaoStock

ymd = datetime.datetime.today().strftime('%Y%m%d_%H%M')
ds = DaoStock

# 매일경제 국내 코스피 전체 주식 목록 URL
url = 'https://stock.mk.co.kr/domestic/all_stocks'

# requests를 사용하여 웹페이지의 내용을 가져옵니다.
response = requests.get(url)

# BeautifulSoup 객체 생성, 'lxml' 파서를 사용하여 파싱
soup = BeautifulSoup(response.text, 'lxml')

divs = soup.find_all("div", class_="st_name")
for i, div in enumerate(divs):
    s_name = div.text.strip()
    s_code = div.find('a')['href'].split("/")[3]
    price  = div.parent.find_all('div')[1].text.strip().replace(",", "")
    cnt = ds.insert()