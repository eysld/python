import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost/static/emp.html"
page = requests.get(url)

soup = bs(page.text, "xml")
print(page.text)
print("=====================================")

