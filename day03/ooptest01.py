class Animal :
    def __init__(self):
        self.life_span = 10
    def fightTiger(self):
        self.life_span = 0
        
class Human(Animal) :
    def __init__(self):
        super().__init__()
        self.money = 0
    def work(self):
        self.money += 30000       
        
if __name__ == '__main__':       
    ani = Animal()
    print("life_span1", ani.life_span)
    ani.fightTiger()
    print("life_span1", ani.life_span)
    
    h = Human()
    print("money",h.money)
    print("life_span1", h.life_span)
    h.fightTiger()
    h.work()
    print("money",h.money)
    print("life_span1", h.life_span)
