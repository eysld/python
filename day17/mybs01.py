import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost/"
page = requests.get(url)
html = page.text

soup = bs(page.text, "lxml")
print(html)
print("=====================================")
# print(soup.find('tr'))
print(soup.find_all('table')[0].find_all('tr')[0])

