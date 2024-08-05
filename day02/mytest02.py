from random import random
arr = [1,2,3]



for i in range(999):
    rnd = int(random()*3)
    a =arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = a

print(arr[0], arr[1])

