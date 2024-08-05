# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
client_id = "Kp3eWz9dXLY8ppP6pCrF"
client_secret = "q_02j7yBO5"
encText = urllib.parse.quote("오류동 맛집")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

response_body = response.read()
html = response_body.decode("utf-8")
soup = bs(html, "xml")
items = soup.find_all('item')
for i,item in enumerate(items):
    title = item.find('title').text
    bloggername = item.find('bloggername').text
    print("{}\t{}\t{}".format(i,title,bloggername))    
