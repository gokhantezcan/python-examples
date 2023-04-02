name = input('adınız nedir? : ')
print(name)


birthYear = input('enter birth year')
age = 2022 - int(birthYear)
print(age)

firstName = "Atilla"
lastName = "İlhan"
formattedMessage = f"{firstName:.2} [{lastName:.3}] is a poet"
print(formattedMessage)


isHot = False
isCold = False

if isHot and isCold:
    print("sicak")
elif  isCold and not isHot:
    print("soguk")
elif  isCold or isHot:
    print("soguk")
else:
    print("hiçbiri")


index = 1
while index < 5:
    print(index)
    index += 1


for index in range(1,9,3):
    print(index)