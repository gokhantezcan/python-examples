from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, licence_plate, color):
        self.wheels_number = 4
        Vehicle.__init__(self, licence_plate, color)

    def get_info(self):
        Vehicle.get_info(self)
        print(f"Araba Tekerlek sayisi {self.wheels_number}")

    def horn(self):
        print("biip")