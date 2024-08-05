# 첫 수를 입력하시오 1
# 끝 수를 입력하시오 4
# 1 에서 4까지 합은 10입니다
a = input("첫 수를 입력하시오")
b = input("첫 수를 입력하시오")
sum = 0

# arr = range(int(a) , int(b)+1)

for i in range(int(a) , int(b)+1) :
    sum += i
print(a,"에서",b,"까지의 합은", sum,"입니다")
