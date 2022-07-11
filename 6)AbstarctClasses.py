#SOYUT KILASLARDAN OBJE YARATILAMAYACAPI İÇİN ANA KLASLARI SOYUTLAŞTIRMAK İÇİN KULLANILAN BİR SİSTEM
#super klaslardan türetilen sub klaslar eğer türetildiği kılas abstrac ise türetildiği klassın bütün değerlerinin eklenmesi gerekir
#abstarct olan klaslarda obje yaratılmaz
#abstarct sahibi ana klasslar şablon yapısı olarak kullanılır ona bağlı kıllaslarda eksik olunup olunmadığını test etmemize yarar
from abc import ABC, abstractclassmethod
#classın içine eklenen @abstaractclassmethod o kılsı soyutlar lakin üstüne yazıldığı defndı bağlanan sub kıllasta yazılmaya zorlar
class Animal(ABC):#super class
    
    @abstractclassmethod
    def walk(self): pass
    @abstractclassmethod
    def run(self): pass
class Bird(Animal):#sub class
    def __init__(self):
        print("bird")

b1 = Bird()