#Elimzideki veriyi yapa class yapısını doğrudan erişimini kapamak ver erişimi kısıtlamak amaçlı kullanılan bir yapı
class BankAccount(object):
    
    def __init__(self, name, money, address):
        self.name = name # GLOBEL
        self.__money = money #PRİVATE #__ Çizgi bir isimlendirmenin yanına gelirse değiştirilemez oluyor.
        self.address = address
    
    #GET VE SET Yapıları priv olan yapıları şekillendirmeye yarar (özel yapıalr değildir ama isimlendirme öyle yapılır)
    def getMoney(self): # Para Öğrenme
        return self.__money

    def setMoney(self, amount):#Para Ekleme Çıkarma
       self.__money = amount
    def getName(self):
        return self.name
    def addressinfo(self):
        return self.address
#kişi verisi
p1 = BankAccount("Erdem", 100000, "Turkey")
 

i = 1
while i == 1: #yapı döngüsü
    b = "  |"
    o = "( "
    ö = ")"
    
    print("|▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂| ")
    print("|                                          |")
    print("|   ⓂⒷ      MİSSBANK HOŞ GELDİNİZ      ⓂⒷ  |")
    print("|▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂| ")
    print("|                                          |")
    print("|    ● Kullanıcı İsmi:",p1.getName(), o, p1.addressinfo(), ö, b)
    print("|------------------------------------------|")
    print("|                 ■ MENÜ ■                 |")
    print("|------------------------------------------|")
    print("| ● Paranızı Görmek İçin (1)               |")
    print("|                                          |")
    print("| ● Paranızı Yatırma İşlemi İçin(2)        |") 
    print("|                                          |")
    print("| ● Para Çekme İşlemi İçin(3)              |")
    print("|------------------------------------------|")

    x = input("İşleminizi Seçin Lütfen: ")

    if x == "1":
        print("Para Miktarı: ", p1.getMoney())

    class islem(object): #par çekme yatırma yapısı
        def __init__(self, a, b):
            self.value1 = a
            self.value2 = b
        def toplama(self):
            result = self.value1 + self.value2
            return result
        def cıkarma(self):
            result = self.value1 - self.value2
            return result

    t2 = p1.getMoney()
    if x == "2":
        t1 = int(input("Kaç TL Eklenecek: "))
        tt = islem(t1, t2)  
        q = tt.toplama()
        p1.setMoney(q)
        print("Yeni Para Miktarı: ", p1.getMoney())




    c1 = p1.getMoney()
    if x == "3":
        c2 = int(input("Kaç TL Çekilecek: "))
        cc = islem(c1, c2)  
        c = cc.cıkarma()
        p1.setMoney(c)
        print("Yeni Para Miktarı: ", p1.getMoney())
    
    print("● İşlemlere Devam Etmek İçin (1) | ● İşlemleri Sonlandırmak İçin (2)")
    s = input("Seçiminiz = ")
    if s == "1":
        i == 1
    if s == "2":
        print("İşlem Sonlandırılıyor...")
        i += 1