from computer import Computer
from keyboard import Keyboard 
from monitor  import Monitor

class Desktop(Computer,Keyboard,Monitor) :
    """Desktop class inherited from Computer, Keyboard, Monitor

    
    has constructor 

    """
    def __init__(self, brand, price, cpu, ram, disk, gpu, kp, alphabet, backlight, ms, mp, mt = "") -> None:
        Computer.__init__(self, brand, price, cpu, ram, disk, gpu)
        Keyboard.__init__(self, brand, kp, alphabet, backlight)
        Monitor.__init__(self, brand, mp, ms, mt)
        self.price = price + kp + mp
        """constructor of Desktop 


        calls computer, keyborad and monitor init methods with self

        sets the price of Desktop with sum of separate parts 
        
        """ 
