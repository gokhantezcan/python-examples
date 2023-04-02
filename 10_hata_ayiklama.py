# -*- coding: utf-8 -*-
try:
    age = int(input("yasinizi giriniz: "))
    print(age)
except ValueError:
    print("yanlıs deger girdiniz.")
except TypeError as exceptiont:
    print("BİR HATA OLUSTU.", exceptiont)
else:
    print("hata almazsa bu kod çalışacak.")
finally:
    print("her durumda çalışır.")
    if("dsflkjsdklf"):
        assert("kosul")
        raise ValueError