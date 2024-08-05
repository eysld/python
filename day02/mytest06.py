# 첫 수를 입력하세요 1
# 끝 수를 입력하세요 5 
# 배수를 입력하세요 2
# 1에서 5까지의 2의 배수의 합은 6입니다
first = int(input("첫 수를 입력하세요"))
last = int(input("끝 수를 입력하세요"))
mul = int(input("배수를 입력하세요"))

sum = 0
for i in range(first, last):
    if i % 2 == 1 : 
        continue
    sum += i
print(str(first)+"에서 "+str(last)+"까지의 "+str(mul)+"의 배수의 합은 "+str(sum)+"입니다")    
