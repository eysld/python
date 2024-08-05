import os
import sys
import urllib.request
import requests
import json
from day17.DaoBlog import DaoBlog
client_id = "Kp3eWz9dXLY8ppP6pCrF"
client_secret = "q_02j7yBO5"
encText = urllib.parse.quote("오류동 맛집")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

response_body = response.read()
my_json = response_body.decode("utf-8")
db = DaoBlog()
data_list = json.loads(my_json)
items = data_list['items']
for i, item in enumerate(items):
    title = item['title']
    link = item['link']
    bloggername = item['bloggername']
    description = item['description']
    bloggerlink = item['bloggerlink']
    postdate = item['postdate']

    db.insert(title, link, description, bloggername, bloggerlink, postdate)