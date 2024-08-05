# com = 1에서 99까지의 수 50
# 수를 입력하세요
# 40 up
# 수를 입력하세요
# 60 down
# 수를 입력하세요
# 50 answer


from random import random
com = int(random()*99)+1

while True:
    mine = int(input("수를 입력하세요"))
    if com >mine :
        print(mine, "up")
    elif com<mine :
        print(mine, "down")
    else :
        print(mine, "answer")
        break