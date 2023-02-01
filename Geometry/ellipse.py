from shape import Shape

class Ellipse(Shape):
    """ellipse class intherited from shape class
    it has a class variable named PI=3
    """
    PI=3
    def __init__(self,r1,r2) -> None:
        super().__init__()
        self.r1=r1
        self.r2=r2
        """constructor of a ellipse
        it calls constructor of super
        it sets r1 and r2 instance variables
        Args:
            r1 (int): radius 1 of ellipse
            r2 (int): radius 2 of ellipse
        """


    def get_area(self):
        return Ellipse.PI*self.r1*self.r2
        """area calculation method
        Returns:
            float: pi * r1 * r2
        """


    
    def change_PI(self,new_PI):
        Ellipse.PI=new_PI    
        """changes the pi class variable 
        it is a class method
        Args:
            new_PI (float): new value of the PI
        """
