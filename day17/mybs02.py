import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost/"
page = requests.get(url)
html = page.text

soup = bs(page.text, "lxml")
print(html)
print("=====================================")
# print(soup.find('tr'))
# print(soup.find_all('tr')[1].find_all('td')[1].text)
trs = soup.find_all('tr')
print(trs)

for i, tr in enumerate(trs):
    if(i == 0):
        continue
    tds = tr.find_all('td')
    myname = tds[1].text
    addr = tds[3].text
    print("{}\t{}".format(myname, addr))
