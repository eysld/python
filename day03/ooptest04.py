class Mavely :
    def __init__(self):
        self.weight = 100
    def eat(self, amount):
        self.weight += amount
        
if __name__ == '__main__':   
    ma = Mavely()
    print(ma.weight)
    ma.eat(50)
    print(ma.weight)
    
    