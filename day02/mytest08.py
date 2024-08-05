# 첫 별수를 입력 3
# 끝 별수를 입력 5
# ★
# a = int(input("첫 별수를 입력"))
# b = int(input("끝 별수를 입력"))
# for i in range(a,b+1) :
#     print("★" * i)


def getStar(cnt):
    ret = ""
    for i in range(cnt):
        ret += "★"
    return ret

a = int(input("첫 별수를 입력"))
b = int(input("끝 별수를 입력"))

for i in range(a, b+1):\
    print(getStar(i))
    