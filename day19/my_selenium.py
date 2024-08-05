from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'http://127.0.0.1/static/emp.html'
driver.get(url)

table = driver.find_element(By.CSS_SELECTOR, "table")
trs = table.find_elements(By.CSS_SELECTOR, "tr")

for i, tr in enumerate(trs):
    if i == 0:
        continue
    
    tds = tr.find_elements(By.CSS_SELECTOR, "td")
    
    myname = tds[1].text
    addr = tds[3].text
    
    print("{}\t{}".format(myname, addr))

sleep(60)