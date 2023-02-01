class Shape:
    """Shape class
    """
    def __init__(self) -> None:
        """constructor of a shape 
            it sets the shape_name instance variable 
        """
        self.shape_name:str = self.__class__.__name__
    def __str__(self) -> str:

        return 'Shape:{},area:{}'.format(self.shape_name,self.get_area())
        """dunder str
        Returns:
            str: 'Shape:<shape name>,area:<area of shape>'
        """


    def get_area(self):
        """area calculation method of a shape
            you should not implement in this class
            dont change 
        """
        pass
