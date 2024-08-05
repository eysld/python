from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

# 웹 사이트에 접근
url = 'https://traffic.daejeon.go.kr/bus/busInfo'
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)

# 웹 페이지의 전체 요소 로드 확인
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "article.busList ul.route")))

# 버스 번호 101을 포함하는 요소 찾기
bus_list = driver.find_elements(By.CSS_SELECTOR, "article.busList ul.route li")
for bus in bus_list:
    bus_number = bus.find_element(By.CSS_SELECTOR, "strong.bus_no")
    if bus_number.text == "101":
        bus_number.click()  # 버스 101 클릭
        break

# 대기 후 페이지 소스 가져오기
sleep(30)

# 클릭 후 페이지 소스 가져오기
page = driver.page_source
soup = BeautifulSoup(page,"lxml")
st = soup.find_all("input", class_="st_name")
# 페이지 소스 출력
print(st) 

driver.quit()
