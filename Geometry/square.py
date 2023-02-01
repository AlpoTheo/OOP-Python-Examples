from rectangle import Rectangle

class Square(Rectangle):
    """Square class inherited from rectangle"""
    
    def __init__(self, a) -> None:
        super().__init__(a,a)
        
        
        

        """constructor method of a square
        it calls constructor method of the super
        Args:
            a (int): one side of a square
        """
