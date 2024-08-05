import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost/"
page = requests.get(url)
html = page.text

soup = bs(page.text, "lxml")
print(html)
print("=====================================")
# print(soup.find('tr'))
trs = soup.select('tr')
for i, tr in enumerate(trs):
    if(i == 0):
        continue
    tds = tr.select('td')
    myname = tds[1].text
    addr = tds[3].text
    print("{}\t{}".format(myname, addr))

