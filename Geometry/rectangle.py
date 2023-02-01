from shape import Shape

class Rectangle(Shape):
    """Rectange class inherited from Shape class
    """
    def __init__(self,a,b) -> None:
        super().__init__()
        self.a=a
        self.b=b
        """constructor of a rectangle
        it calls the constructor of super
        it sets the a and b instance variables 
        Args:
            a (int): a side of a rectangle
            b (int): b side of a rectangle
        """


    def get_area(self):
        return self.a*self.b
        """area calculation method
        Returns:
            int: area of the rectangle
        """
