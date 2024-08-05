from random import random
arr = list(range(1,9+1))



for i in range(999):
    rnd = int(random()*9)
    a =arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = a

print(arr[0], arr[1], arr[2])

