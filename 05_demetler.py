# -*- coding: utf-8 -*-
numbers = (1,2,3,3) # elemanlarını silemeyiz. yeni eleman ekleyemeyiz. değerleri değiştiremeyiz.
print(numbers)
# listelerden daha hızlıdır.

tuple1 = ("ege") # 1 eleman olursa onun değerini alır.
tuple2 = ("ege", "ahmet")
print(tuple1)
print(tuple2)

evenNumberList = [number for number in range(2,101,2)]
evenNumberTuple = tuple(evenNumberList)
print(evenNumberTuple)

stringValue = "python"
stringTuple = tuple(stringValue)
stringList = list(stringValue)
print(stringTuple)