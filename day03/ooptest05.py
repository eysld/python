from day03.ooptest03 import Wonbin
from day03.ooptest04 import Mavely
class YoungHun(Wonbin, Mavely):
    def __init__(self):
        # super().__init__()
        Wonbin.__init__(self)
        Mavely.__init__(self)
    
    
    
    
if __name__ == '__main__':
    yh = YoungHun()
    print("ugly",yh.flag_ugly)
    print("weight",yh.weight)
    yh.plastic()
    yh.eat(5)
    print("ugly",yh.flag_ugly)
    print("weight",yh.weight)