# -*- coding: utf-8 -*-

from random import choice

def greetUser(firstname, lastname):
    print("merhaba")
    print(lastname)
    
greetUser(lastname = "gokhan", firstname="fdsgfd")

# aşağıdaki kod farklı adresleri yazacaktır. yani değerler birer nesne olluyor.
# değişkenler sayılmıyor. c++ dan farklı budur.
string1 = "gokhan"
print(id(string1))
string1 = "deneme"
print(id(string1))

# if string1 is - is not string2  --> adreslerini karşılaştırmak için kullanılır.
# == değerleri ancak is ise idleri karşılaştıracaktır bilgin olsun (sınıfları karşılaştırır)
# if string1 is None --> içeriğide birsey yok yani yani null gibi oluyor burada

def naber(firstname: str, yas: int, mesaj : str = "defaultValue"):
    print("degerlerin durumlarını soyluyorsun")
    
variable1 = 1
variable2 = 2

temporary = variable1
variable1 = variable2
variable2 = temporary
print(variable1, variable2)

def denetle(isim: str) -> bool:
    return False

print(denetle("gokhanhan"))


message = "c"
def yaz():
    global message # global değişkeni almaktadır.
    message = "a"
def yazdir():
    message = "b"
    
     
    
    
    
    
    
    
    
    