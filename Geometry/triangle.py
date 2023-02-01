from rectangle import Rectangle

class Triangle(Rectangle):
    """Triangle class inherited from rectangle"""
    
    def __init__(self, a, b) -> None:
        super().__init__(a,b)
        """constructor of a Triangle
            it calls the constructor of super
            
        Args:
            a (int): height of a Triangle
            b (int): base of a Triangle
        """


    def get_area(self):
        return self.a*self.b/2
        """area calculation method
        Returns:
            int: area of the Triangle
        """
