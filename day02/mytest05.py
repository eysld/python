# 가위/바위/보를 선택하세요
# 나 : 가위
# 컴 : 보
# 결과 : 이김
from random import random
mine =  input("가위/바위/보를 선택하세요")
rnd = random()
if rnd > 0.66 :
    com = "가위"
elif rnd > 0.33 :
    com = "바위"
else :
    com = "보"

print("mine", mine)
print("com", com)

if (mine == "가위" and com == "바위") or (mine == "바위" and com == "보") or (mine == "보" and com == "가위"):
    print("결과 : 짐")
elif (mine == "가위" and com == "보") or (mine == "바위" and com == "가위") or (mine == "보" and com == "주먹"):
    print("결과 : 이김")
else :
    print("결과 : 비김")
    
