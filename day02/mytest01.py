# 홀/짝을 입력하시오
from random import random
mine = input("홀/짝을 입력하시오")
if random()>0.5 :
    com = "홀"
else :
    com = "짝"

if mine == com :
    print("결과 : 이김") 
else :
    print("결과 : 짐") 
       