#initler or contructor class içinde değiştirilebilir özellikleri belirtir
#self yapısı ise bulunduğu classın iç değerleri olduğunu belirtir örn: selfyaş=yaş classın yaşının dışrdan gelen yaşa eşitlenmesidir
class Çalışan(object):
    def __init__(self, name, eight, age, money, year):
        self.isim= name
        self.boy = eight
        self.yaş = age
        self.maaş= money
        self.çalışma_yılı=year
        
    def getisim(self):
        return self.isim

    def getboy(self):
        return self.boy
    
    def getyaş(self):
        return self.yaş
    
    def getmaaş(self):
        return self.maaş
    
    def getçalışmayılı(self):
        return self.çalışma_yılı
a1= Çalışan("erdem", 180, 20, 2000, 1)
a2= Çalışan("fisun", 170, 42, 5000, 10)
a3= Çalışan("akın", 155, 60, 7000, 20)

print(a1.getisim())
print(a2.getmaaş())
print(a3.getyaş())

