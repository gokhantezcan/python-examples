# -*- coding: utf-8 -*-

def Decoratorfunction(originalFunction):
    
    def Wrapperfunction():
        print("wrapper işleri")
        print(f"orijinal fonksiyon ' {originalFunction.__name__}' öncesi")
        return originalFunction()
    
    return Wrapperfunction

@Decoratorfunction
def Myfunction():
    message = "bazı işler yapıyorum"
    print(message)

Myfunction()