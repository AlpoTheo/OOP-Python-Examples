from datetime import date
 
class Service:
    """Tamir servisi işlemlerini yapan sınıf"""

    """işçilik ücreti oranını ve servisin adını class variable olarak tanımlayıp, 
    ilk değerlerini giriniz. """ 


    """ price_list dictionary'si class variable olarak tanımlanmıştır
        üzerinde herhangi bir değişiklik yapmayınız
        yapılan işlemin ücretini hesaplamak için faydalanmalısınız.
    """
    service_name=str
    workmanship_rate=0
    price_list = {
        "yag":400,
        "yag_filtresi":75,
        "hava_filtresi":110,
        "polen_filtresi":60,
        "yikama":50,
        "motor_temizligi":100,
        "buji":600,
        "aku":1500,
        "balata":750,
        "disk":1600,
        "triger":1250,
    }

    def __init__(self, plate_no:str, name_surname:str, work_list=[]) -> None:
        self.plate_no=plate_no
        self.tamad=name_surname
        self.work_list=work_list
        value=name_surname.split(" ")
        self.name=value[0]
        self.surname=value[1]
        self.complete=[]
        self.total_price=0
        
        
        
        """Service constructor
        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str]): yapılacak iş listesi
        """
        

    @classmethod
    def onbin(cls,plate_no:str, name_surname:str, work_list=[]):
        work_list=["yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        return cls(plate_no,name_surname,work_list)

        """onbin bakımı için ön tanımlı iş listesine sahip constructor overload
        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].
        ön tanımlı iş listesi["yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """
        
    
    @classmethod
    def yirmibin(cls,plate_no:str, name_surname:str, work_list=[]):
        work_list=["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        return cls(plate_no,name_surname,work_list)
        """yirmibin bakımı için ön tanımlı iş listesine sahip constructor overload
        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].
        ön tanımlı iş listesi["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """ 
    
    @classmethod
    def otuzbin(cls,plate_no:str, name_surname:str, work_list=[]):
        work_list=["motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        return cls(plate_no,name_surname,work_list)
        """otuzbin bakımı için ön tanımlı iş listesine sahip constructor overload
        Args:
            plate_no (str): plaka no
            name_surname (str): isim soyisim
            work_list (list[str], optional): yapılacak iş listesi varsayılan değeri [].
        ön tanımlı iş listesi["triger","buji","motor_temizligi","balata","disk","yag","yag_filtresi","hava_filtresi","polen_filtresi","yikama"]
        Returns:
            Service: geriye service türünde bir örnek döndürüyor
        """ 
    
    @property
    def name_surname(self) -> str:
        return  "{}{}{}*** {}{}{}***".format(self.name[0],self.name[1],self.name[2],self.surname[0],self.surname[1],self.surname[2])
        """name_surname getter
        Returns:
            str: __name ve __surname gizli değişkenlerinde tutulan anonimleştirilmiş isim ve soy ismi geriye döndürür
            örnek: Ala*** Uça***
        """ 

    @name_surname.setter
    def name_surname(self,value:str) -> None:
        value=value.split(" ")
        self.name=value[0]
        self.surname=value[1]
        
        """name_surname setter
        Args:
            value (str): içerisine isim ve soyisim alıyor ve __name ve __surname gizli değişkenlerine atama yapıyor.
        """ 

    @classmethod
    def set_workmanship_rate(cls,workmanship_rate:float) -> None:
        cls.workmanship_rate=workmanship_rate 
        """işçilik oranı class variable ını değiştiren class method
        Args:
            workmanship_rate (float): işçilik oranı
        """ 

    @classmethod
    def set_service_name(cls,service_name) -> None:
        cls.service_name=service_name
        """servis adı class variable nı değiştiren class method
        Args:
            service_name (_type_): servis adı 
        """ 

    def do_worklist(self):
        for i in self.work_list:
            price=self.price_list.get(i)
            workmanship=price*self.workmanship_rate
            self.total_price += (workmanship+price)
            self.complete.append("*{},{}tl,{}tl".format(i,price,workmanship))


            

        """iş listesinde yer alan her işçilik kalemi için
           önce işin fiyatını bulur
           sonra işçilik oranına göre işçilik ücretini hesaplar
           yapılan işler listesine ekler
        """ 

    def print(self) -> None:
        print("--------------------")
        print("{}-{}-{}".format(self.plate_no,self.name_surname,date.today()))
        for i in self.complete:
            print(i)
        print("İşçilik Oranı:{}".format(self.workmanship_rate))
        print("Toplam:{}tl".format(self.total_price))
        print("Servis:{}".format(self.service_name))
        print("--------------------")

        

        """serviste yapılan işlerin ücret özetini ekrana basar
        format:
            20 tane -
            <plaka>-<anonimleştirilmiş isim soy isim>-<bugünkü tarih, yıl,ay,gün>
            başında * ile yapılan her bir işlemi alt alta *<work>,<price>tl,<workmanship>tl
            İşçilik Oranı: <workmanship_rate>
            Toplam: <toplam_tutar>tl
            Servis: <service_name>
            20 tane -
        """ 
        

    
    def anonymize(_in) -> str:
        """Gelen stringin ilk üç harfini alır ve 
        sonuna *** ekleyerek anonimleştirme işlemi gerçekleştirir.
        Bu bir static methoddur.
        Args:
            _in (str): gelen string
        Returns:
            str: anonimleşmiş string
        """ 
