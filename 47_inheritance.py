from Bike import Bike
from Car import Car
from Bus import Bus
from Convertible import Convertible
from Van import Van

bike1 = Bike("34ert67", "Beyaz")
bike1.get_info()
bike1.accelerate()
bike1.get_info()
bike1.brake()
bike1.get_info()
print(bike1.wheels_number)


car1 = Car("34ert67", "Beyaz")
car1.get_info()
car1.accelerate()
car1.get_info()
car1.brake()
car1.get_info()
print(car1.wheels_number)

bus = Bus("34ert67", "Beyaz")
bus.get_info()
bus.accelerate()
bus.get_info()
bus.brake()
bus.get_info()
print(bus.wheels_number)

cv1 = Convertible("34ert67", "Beyaz")
cv1.get_info()
cv1.accelerate()
cv1.get_info()
cv1.brake()
cv1.get_info()
print(cv1.wheels_number)

van1 = Van("34ert67", "Beyaz")
van1.get_info()
van1.accelerate()
van1.get_info()
van1.brake()
van1.get_info()
print(van1.wheels_number)
print(van1.seats_number)

