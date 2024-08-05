from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'http://127.0.0.1/static/emp.html'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, "lxml")
table = soup.select_one('table')
trs = table.select('tr')
for i, tr in enumerate(trs):
    tds = tr.select('td')
    myname = tds[1].text
    addr = tds[3].text
    print("{}\t{}".format(myname,addr))

sleep(60)