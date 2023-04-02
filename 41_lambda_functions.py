# -*- coding: utf-8 -*-
# bir kere kullanıp çöpe atacak isek def yerine lambda kullanabiliriz.
f = lambda x: 3*x + 2
print(f(2))
print((lambda x: 3*2 + 2)(2))
f = lambda : "gokhan"
print(f())
