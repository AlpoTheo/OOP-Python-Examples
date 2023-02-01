from hardware import Hardware
class Monitor(Hardware):
    """Monitor class inherited from hardware

    has constructor 
    """
    def __init__(self,brand,price,ms,mt ) -> None:
        Hardware.__init__(self,brand,price)
        self.ms = ms
        self.mt = mt
        """Monitor constructor

        Args:
            brand (str): brand of Monitor
            price (int): price of Monitor
            monitor_size (str): size of Monitor 
            monitor_type (str): type of Monitor 
        """ 


