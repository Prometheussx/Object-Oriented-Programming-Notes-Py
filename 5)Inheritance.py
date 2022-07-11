#Miras yapısı elimizdeki ana kalsmandaki bilgileri alt kılasmandaki farklı birimelerle ortak olanlarının çekilip kullanılmasını sağalr yani
#her hayvan nefes alabilir kuş uçar maymun tırmanır bu iki alt kılasmandaki ortan nefes almayı ana kılasmandan çekip kullanabiliriz

class Animal(object):
    def __init__(self):
        print("Creat Animal")

    def toString(self):
        print("animal")
    
    def walk(self):
        print("Animal walk")

class monkey(Animal):
    def __init__(self):
        super().__init__()
        print("creat monkey")
   
    def toString(self):
        print("monkey")

    def climb(self):
        print("monkey can climb")

class bird(Animal):
    def __init__(self):
        super().__init__()
        print("creat bird") 
    
    def fly (self):
        print("bird can fly")
b1=bird()
m1= monkey()
m1.toString()
b1.fly()
m1.climb()
m1.walk()