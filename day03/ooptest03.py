class Wonbin :
    def __init__(self):
        self.flag_ugly = True 
    def plastic(self):
        self.flag_ugly = False

if __name__ == '__main__':   
    won = Wonbin()
    print(won.flag_ugly)
    won.plastic()
    print(won.flag_ugly)