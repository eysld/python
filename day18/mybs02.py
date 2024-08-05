import requests
from bs4 import BeautifulSoup
import datetime

# 매일경제 국내 코스피 전체 주식 목록 URL
url = 'https://stock.mk.co.kr/domestic/all_stocks'

# requests를 사용하여 웹페이지의 내용을 가져옵니다.
response = requests.get(url)

# BeautifulSoup 객체 생성, 'lxml' 파서를 사용하여 파싱
soup = BeautifulSoup(response.text, 'lxml')

# 현재 시간을 'YYYYMMDDHHMMSS' 형식으로 포맷
current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# 주식 이름, 코드, 가격을 함께 출력
stocks = soup.find_all('span', class_='name')
prices = soup.find_all('div', class_='st_price')

for stock, price_div in zip(stocks, prices):
    a_tag = stock.find('a')
    if a_tag and price_div:
        name = a_tag.text.strip()  # 종목 이름
        href = a_tag['href']  # a 태그의 href 속성
        code = href.split('/')[-1]  # href에서 종목 코드 추출
        price = price_div.find('span', class_='price').text.strip()  # 주식 가격 텍스트
        print("{}\t{}\t{}\t{}".format(code, name, price, current_time))
