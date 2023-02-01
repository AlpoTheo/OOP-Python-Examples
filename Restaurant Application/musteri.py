from yemek import Yemek
from adres import Adres

class Musteri(Adres):
    def __init__(self,adi,soyadi,bakiye,il,ilce) -> None:
        super().__init__(il,ilce)
        self.adi=adi
        self.soyadi=soyadi
        self.bakiye=bakiye
        self.yemekler=[]

    def siparis_ekle(self,yemek):
        self.yemekler.append(f'*yemek:{yemek.yemek},{yemek.fiyat}tl')
        self.bakiye -= yemek.fiyat

    def __str__(self) -> str:
        new_str = f'ad:{self.adi},soyad:{self.soyadi},bakiye{self.bakiye}\n'
        new_str += f'adres:{self.il}-{self.ilce}\n'
        for i in self.yemekler:
            new_str += i+'\n'
        return new_str