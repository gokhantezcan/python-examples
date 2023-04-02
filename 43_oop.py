class MyClass:
    classAttribute = "Merhaba"

    def MyMethod(self, param):
        self.instanceAttribute = param

myInstance = MyClass()

MyClass.classAttribute = "Merhaba"
myInstance.instanceAttribute = "Dunya"

# instance her iki attribute a erişebilir ancak Myclass instance attribute ına erişemez.
# instance değelrleri sınıfın değerlerinde önceliklidir. bunu unutma.
print(MyClass.classAttribute, myInstance.instanceAttribute)

print("*****")
myInstance1 = MyClass()
myInstance1.MyMethod("Dunya")
print(myInstance1.classAttribute)
print(myInstance1.instanceAttribute)
print(MyClass.classAttribute)