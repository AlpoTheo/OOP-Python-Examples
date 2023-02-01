from ellipse import Ellipse

class Circle(Ellipse):
    """circle class inherited from ellipse"""

    
    def __init__(self, r) -> None:
        super().__init__(r,r)
        """constructor of circle 
        it calls constructor of super
        Args:
            r (int): radius of circle
        """
