class Hesap: 
    """Hesap ve harcama bilgilerini tutan sınıf"""

    def __init__(self,ad,soyad,baslangic_bakiyesi) -> None:
        self.isim=ad
        self.soyisim=soyad
        self.baslangic_bakiyesi=baslangic_bakiyesi
        self.para=baslangic_bakiyesi
        self.kayit = []


    @property
    def ad(self):
        return "{}{}{}***".format(self.isim[0],self.isim[1],self.isim[2])

        """ad property getter
        Returns:
            str: adın ilk üç harfi ve 3 yıldız
            örnek: Ayş***
        """ 
    @ad.setter
    def ad(self,value):
        self.isim=value
        
        
        """ad setter
        Args:
            value (str): kişi adı
        """ 
    @property
    def soyad(self):
        return "{}{}{}***".format(self.soyisim[0],self.soyisim[1],self.soyisim[2])
        """soyad setter
        Returns:
            str: soyadın ilk üç harfi ve 3 yıldız
            örnek: Yıl***
        """ 
    @soyad.setter
    def soyad(self,value):
        self.soyisim=value
        """soyad setter
        Args:
            value (str): kişi soyadı
        """ 
    @property
    def bakiye(self):
        return float(self.para)

        """bakiye property
        Returns:
            float: kişi bakiyesi
        """ 
    @bakiye.setter
    def bakiye(self,value):
        raise AttributeError("Bakiye değiştirilemez!")
        """bakiye setter
        Args:
            value (float): bakiye property si read-only dir
        Raises:
            AttributeError: Bakiye değiştirilemez!
        """ 

    def __hareket_ekle(self,aciklama,miktar):
        self.kayit.append(aciklama)
        self.kayit.append(miktar)
        """hareket ekle methodu
        Args:
            aciklama (str): hareket açıklaması
            miktar (float): miktar 
        """ 

    def yatir(self,value):
        if (value<0):
            raise AttributeError("Yatırılan miktar 0'dan büyük olmalıdır!")
        else:
            self.kayit.append("Para Yatırma")
            self.kayit.append(value)
            self.para+=value
        
        """para yatirma methodu
        Args:
            value (float): yatan miktar
        miktar negatif olursa aşağıdaki hata gerçekleşmelidir.
        Raises:
            AttributeError: Yatırılan miktar 0'dan büyük olmalıdır!
        """ 

    def harca(self,aciklama,miktar):
        if (miktar < 0):
            raise AttributeError("Harcanan miktar 0'dan büyük olmalıdır!")
        elif (miktar > self.para):
            raise AttributeError("Bakiye yetersiz!")
        else:
            self.para-=miktar
            self.__hareket_ekle(aciklama,-miktar)
        """harcama methodu
        Args:
            aciklama (str): harcama açıklaması
            miktar (float): miktar
            miktar negatif olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Harcanan miktar 0'dan büyük olmalıdır!
        
            miktar bakiyeden büyük olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Bakiye yetersiz!
        """ 

    def dokum(self):
        print("--------------------")
        print("{},{}".format(self.ad, self.soyad))
        print("*Başlangıç bakiyesi,{}".format(self.baslangic_bakiyesi))
        i=0
        while (i<len(self.kayit)):
            print("*{},{}".format(self.kayit[i], self.kayit[i+1]))
            i+=2
        print("Hesap Bakiyesi:{}".format(self.para))
        print("--------------------")
        """hesap dokumu methodu 
        önce ------ yazar 20 çizgi
        sonra kişinin adı ve soyadı yazar
        sonra tüm hareketler alt alta yazılır
        sonra hesap bakiyesi yazılır
        sonra ------ yazar 20 çizgi
        
        """ 
