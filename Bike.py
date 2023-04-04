from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, licence_plate, color):
        self.wheels_number = 2
        Vehicle.__init__(self, licence_plate, color)

    def get_info(self):
        Vehicle.get_info(self)
        print(f"Bisiklet Tekerlek sayisi {self.wheels_number}")

    def horn(self):
        print("horn")