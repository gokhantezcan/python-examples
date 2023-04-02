numbers = [1,2,3]
letters = ['a', 'b', 'c']
summations = numbers + letters
summations.append('pyhton')
print(summations)
print(4 * letters)

squares = []
for number in numbers:
    squares.append(number**2)
print(squares)

squares2 = [number**3 for number in numbers]
print(squares2)

liste3 = [number for number in range(2, 1001, 2) if number % 3 == 0]
print(liste3)

list1 = [1,2,3]
list2 = [4,5,6]
newList = [x * y for x in list1 for y in list2 if x * y <= 10]
print(newList)

if 8 in newList:
    print("8 bu listede var.")

coordinates = [5,3,4,6,8,9,0]
x,y,z = coordinates[0:3]
print(x*y*z)
