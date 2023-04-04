from Vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, licence_plate, color):
        self.wheels_number = 4
        Vehicle.__init__(self, licence_plate, color)
        self.seats_number = 12

    def get_info(self):
        Vehicle.get_info(self)
        print(f"Otobus Tekerlek sayisi {self.wheels_number}")

    def horn(self):
        print("büüp")