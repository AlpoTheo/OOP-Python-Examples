class Hardware:
    """Hardware base class"""

    def __init__(self,brand,price) -> None:
        self.brand=brand
        self.price=price
        """hardware constructor

        Args:
            brand (str): brand of hardware
            price (int): price of hardware
        """ 