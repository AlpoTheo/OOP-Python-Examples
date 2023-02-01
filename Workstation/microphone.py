from hardware import Hardware

class Microphone(Hardware):
    """Microphone class inherited from hardware

    has constructor 
    """
    def __init__(self,brand,price,mctype) -> None:
        Hardware.__init__(self,brand,price)
        self.mctype=mctype
        """Microphone constructor

        Args:
            brand (str): brand of Microphone
            price (int): price of Microphone
            microphone_type (str): type of Microphone 
        """ 
