# -*- coding: utf-8 -*-

class Calc(object):
    #init metodu
 def __init__(self, a, b):
      "initialize values" #def içi komut açıklayıcısı
      
      #atribute  
      self.value1 = a
      
      self.value2 = b
      
      
 def add(self):
          "addition a+b = result" #def içi komut açıklayıcısı
          result = self.value1 + self.value2
          return result
        
 def multiply(self):
          "multiplication a*b = result => result" #def içi komut açıklayıcısı
          result = self.value1 * self.value2
          return result

print("Choose add(1), Multiply(2)")
select = input("Select 1 or 2: ")

v1 = int(input("Value 1: "))
v2 = int(input("Value 2:"))

c1 = Calc(v1,v2)

if select == "1":

   add_result = c1.add()
   print(add_result)

elif select == "2":
    multiply_result = c1.multiply()
    print(multiply_result)