class Mixture:
    """Salt and water mixture manipulation class"""

    def __init__(self,total_amount:float,salt_amount:float) -> None:
        self.toplamtutar=total_amount
        self.tuzmiktari=salt_amount
        """Mixture Constructor
        Args:
            total_amount (float): water + salt amount
            salt_amount (float): salt amount
        """


    @property
    def salt_ratio(self):
        return self.tuzmiktari/self.toplamtutar
        """salt_ratio property getter
        Returns:
            float: salt_amount / total_amount
        """


    @salt_ratio.setter
    def salt_ratio(self,value):
        x = self.toplamtutar * value
        self.toplamtutar += x
        self.tuzmiktari += x


        """salt_ratio property setter
        Calculates salt_amount with salt_ratio and total_amount 
        and sets salt_amount 
        Args:
            value (float): salt ratio
        """


    @property
    def water_amount(self):
        return self.toplamtutar-self.tuzmiktari
        """water_amount property getter
        Returns:
            float: total_amount - salt_amount
        """   


    @water_amount.setter
    def water_amount(self,value):
        raise AttributeError("Cannot set water amount")
        """water_amount property setter
        water_amount is a calculated property 
        it is read-only
        Args:
            value (float): water amount (but not used)
        Raises:
            AttributeError: "Cannot set water amount"
        """


    @property
    def water_ratio(self):
        return 1-self.salt_ratio
        """water_ratio property getter
        Returns:
            float: 1 - salt_ratio
        """


    @water_ratio.setter
    def water_ratio(self,value):
        raise AttributeError("Cannot set water ratio")

        """water_ratio property setter
        water_ratio is a calculated property 
        it is read-only
        Args:
            value (float): water ratio (but not used)
        Raises:
            AttributeError: "Cannot set water ratio"
        """


    @classmethod
    def from_salt_ratio(cls,total,salt_ratio):
        salt=total*salt_ratio
        return cls(total,salt)
        
        """from_salt_ratio is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and 0 salt_amount
        and creates a new instance
        it sets salt_ratio property of new instance
        Args:
            total_amount (float): water + salt amount
            salt_ratio (float): salt ratio
        Returns:
            Mixture: created new instance 
        """


    @classmethod
    def from_water_ratio(cls,total,water_ratio):
        salt=total-(total*water_ratio)
        return cls(total,salt)
        """from_water_ratio is a classmethod 
        it is a alternative constructor
        it calls from_salt_ratio alternative constructor with total_amount and 1-water_ratio 
        Args:
            total_amount (float): water + salt amount
            water_ratio (float): water ratio
        Returns:
            Mixture: created new instance 
        """


    @classmethod
    def from_water_amount(cls,total,water):
        salt=total-water
        return cls(total,salt)
        """from_water_amount is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and total_amount-water_amount
        and creates a new instance 
        Args:
            total_amount (float): water + salt amount
            water_amount (float): water amount
        Returns:
            Mixture: created new instance 
        """


    @classmethod
    def from_amounts(cls,water,salt):
        return cls(water+salt,salt)
        """from_amounts is a classmethod 
        it is a alternative constructor
        it calls main constructor with water_amount+salt_amount and salt_amount
        and creates a new instance 
        Args:
            water_amount (float): water amount
            salt_amount (float): salt amount
        Returns:
            Mixture: created new instance 
        """


    def __add__(self,rhs):
        total=self.toplamtutar+rhs.toplamtutar
        salt=self.tuzmiktari+rhs.tuzmiktari
        return Mixture (total,salt)
        

        """Mixture class + operator overloader
        it creates a new instance with self.total_amount + rhs.total_amount and self.salt_amount + rhs.salt_amount
        Args:
            rhs (Mixture): right hand side object
        Returns:
            Mixture: created new instance
        """


    def __truediv__ (self,value):
        total= self.toplamtutar/value
        salt= self.tuzmiktari/value
        return Mixture(total,salt)
        
        """Mixture class / operator overloader
        it creates a new instance with self.total_amount / value and self.salt_amount / value
        Args:
            value (float): divider
        Returns:
            Mixture: created new instance
        """


    def __mul__(self,value):
        total=self.toplamtutar*value
        salt=self.tuzmiktari*value
        return Mixture(total,salt)
        """Mixture class * operator overloader
        it creates a new instance with self.total_amount * value and self.salt_amount * value
        Args:
            value (float): multiplier
        Returns:
            Mixture: created new instance
        """


    def __eq__(self,rhs) -> bool:
        if self.toplamtutar==rhs.toplamtutar and self.tuzmiktari==rhs.tuzmiktari:
            return True
        else:
            return False
            
        """Mixture class == operator overloader
        Args:
            rhs (Mixture): right hand side object
        Returns:
            bool: self.total_amount == rhs.total_amount and self.salt_amount == rhs.salt_amount
        """

        

    def __str__(self) -> str:
        return f"SA:{self.tuzmiktari:3.2f},WA:{self.water_amount:3.2f},SR:{self.salt_ratio:3.2f},WR:{self.water_ratio:3.2f},TOTAL:{self.toplamtutar:3.2f}"
        """Mixture class to string method overloader
        Returns:
            str: 'SA:{:3.2f},WA:{:3.2f},SR:{:3.2f},WR:{:3.2f},TOTAL:{:3.2f}'
        """
