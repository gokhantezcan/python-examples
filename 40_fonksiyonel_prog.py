# -*- coding: utf-8 -*-

# bir fonksiyona deger olarak baska bir fonksiyon verilebilir.
#fonksiyon veri yerine kullanılabilir.


def calculate(func, x, y):
    return func(x,y)


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

print(calculate(add, 9,4))
print(calculate(subtract, 9,4))

# fonksiyon içinde fonksiyon
def helloworld(param):
    def World(world):
        print(param, world)
    return World

f = helloworld("hello")
f("World")

def actionOne(param):
    print(param)

def actionTwo(param):
    print(param)

myFunclist = [actionOne, actionTwo]
myFunclist[0]("deneme")



def sampleFunc(callback):
    print("bazı işler yap")
    return callback

def Callback(message):
    print(message)

f = sampleFunc(Callback)
f("merhaba dunya")    










