
def goster(*args):
    for arg in args:
        print(arg)

goster("ahmet", "mehmet", 12)
goster(23, True)
liste = ["ahmet", "mehmet", 12]

goster(*liste)

print("--------------------------------------")

def properCalorie(**fruits):
    print(fruits)
    print(type(fruits))

properCalorie(ananas = 52, kivi = 49)
myFurits= {"ananas": 52, "kivi": 49, "nar": 63, "greyfurt": 41}
properCalorie(**myFurits)