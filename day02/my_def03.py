from random import random
def getHJ():
    if random()>0.5 :
        return "홀"
    else :
        return "짝"
com = getHJ()
print("com", com)