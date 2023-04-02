# -*- coding: utf-8 -*-

names = ["gokhan", "ahmet", "selim"]
print(names[-1])

matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

for row in matrix:
    for item in row:
        print(item)
        
# insert append, remove, pop, clear, index, count (kaç tane var), 
# sort, reverse, len
        
#matrix2 = matrix; bu atamada aşağısı aynı çalışır.
matrix2 = matrix.copy()
matrix.append(15)
print(matrix)
print(matrix2)