from square import Square

class Cube(Square):
    """Cube class inherited from square class"""
    
    def __init__(self, a) -> None:
        super().__init__(a)
        self.a=a
        """constructor of a cube 
            it calls constructor of super
        Args:
            a (int): one side of a cube
        """


    def get_volume(self):
        return self.a*self.a*self.a
        """calculates volume of cube 
        Returns:
            int: volume of cube
        """


    def __str__(self) -> str:
        return 'Shape:{},volume:{}'.format(self.shape_name,self.get_volume())
        """dunder str
        Returns:
            str: 'Shape:<shape name>,volume:<volume of cube>'
        """
