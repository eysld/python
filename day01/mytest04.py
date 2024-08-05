#출력할 단수를 입력하세요 4
a = int(input("출력할 단수를 입력하세요"))
arr = range(1, 9+1)
for i in arr :
    print(a,"*",i,"=",a * i)