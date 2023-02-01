from desktop import Desktop
from camera import Camera
from microphone import Microphone

class Workstation(Desktop,Camera,Microphone):
    """Workstation class inherited from Desktop, Camera, Microphone

    """

    def __init__(self, brand, price, cpu, ram, disk, gpu, kp, alphabet, backlight, cp, resolution, mcp, mctype, ms, mp, mt = "") -> None:
        Desktop.__init__(self, brand, price, cpu, ram, disk, gpu, kp, alphabet, backlight, ms, mp)
        Camera.__init__(self, brand, price,resolution)
        Microphone.__init__(self, brand, price, mctype)
        self.price = price + kp + cp + mcp + mp
        """constructor of Workstation 


        calls Desktop, Camera and Microphone init methods with self

        sets the price of Workstation with sum of separate parts 
        
        """
 