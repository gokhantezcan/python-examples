from Car import Car
from Bus import Bus

class Van(Car, Bus):
    def __init__(self, licence_plate, color):
        Bus.__init__(self, licence_plate, color)
        Car.__init__(self, licence_plate, color)