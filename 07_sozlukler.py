# -*- coding: utf-8 -*-
customer = {
        "name" : "fernah",
        "email" : "dsflkjlkds",
        "tel" : "fdgkfdlşg"
        }
customer2 = dict(name="dsfsd", email = "dfdsfds", tel= "dsfds")

customer["id"] = 5

print(customer["id"])

if "date" in customer:
    print(customer["date"])
else:
    print("date alanı yok")
    
print(customer.get("deger"))
print(customer.get("name", "dsfdsf")) # name oldugu için default degeri atamadı.

for key in customer:
    print(key)
print("*******")
for key in customer.keys():
    print(key)

customerItem = list(customer.items())
print(customerItem)

for key, value in customerItem:
    print(f"{key}={value}")
    
customer.pop("name") # name silinir.
customer.popitem() # sondan bir key value silinir.
# del(customer), customer.update(name2 = "dsfjkdshfkj")


