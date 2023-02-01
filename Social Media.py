class SosyalMedya:
    """Sosyal Medya hesaplarındaki takip durumunu kontrol eden sınıf"""
    hesapadi:str=""
    gercekadi:str=""
    takipci_sayisi=int
    takibi_birakan=int
    
    def __init__(self,hesapadi,gercekadi,takipci_sayisi):
       self.hesapadi=hesapadi
       self.gercekadi=gercekadi
       self.takipci_sayisi=takipci_sayisi
       self.takibi_birakan=0


    
    def takip_et(self):
        """hesabın takipçi sayısını 1 artıran method"""
        self.takipci_sayisi=self.takipci_sayisi+1
        


    def takibi_birak(self):
        """hesabın takipçi sayısını 1 azaltan method (takipci sayısı negatif olamaz)"""
        if (self.takipci_sayisi>0):
            self.takipci_sayisi-=1
            self.takibi_birakan+=1

    def takipci_durumu(self):
        """hesap adı,gerçek adı,takipçi sayısı ve takibi bırakan sayısını ekrana basan method"""
        print("{},{},{},{}".format (self.hesapadi,self.gercekadi,self.takipci_sayisi,self.takibi_birakan))