# -*- coding: utf-8 -*-
# kümelerde mükerren item bulunamaz.
numbers = [1,1,2,3,4,5]
uniques = set(numbers)
print(uniques)

# asagıdaki gibi boş alanlar acabilirsin.
sampSet = set()
sampleList = list()
sampleTuple = tuple()

uniques.discard(100) # olmayanı silmek istediğinde hata vermez.
uniques.pop() # sadece kümeden eleman silmek için kullanılır. hangisi siliniyor bilinmez
uniques.update({23,89})
print(uniques)
del(uniques) # direkt kümeyi siler. clean metodu ise kumeyi boşaltır.

evenNumber = {number for number in range(2, 51, 2)}
oddNumber = {number for number in range(1, 51, 2)}
print(evenNumber | oddNumber) # iki kümenin birleşimini vermektdir.
print(evenNumber.union(oddNumber))
print(evenNumber & oddNumber)
print(evenNumber.intersection(oddNumber))
print(evenNumber - oddNumber)
print(evenNumber.difference(oddNumber))


sampleSet = {3,5,1}

if sampleSet.issubset(oddNumber): # alt küme tanımıdır. <= da kullanılmaktadır. < öz alt küme için.
    print("success")
    
if oddNumber.issuperset(sampleSet):
    print("success")

if sampleSet == oddNumber:
    print("iki küme eşittir.")

vowels = {'a', 'e', 'i', 'o', 'u'}
string = "pyhton is awesome"
stringSet = set(string)
stringVowels = stringSet & vowels
print(stringVowels)

if 'i' in stringVowels:
    print("ok")

for character in stringVowels:
    print(character)

