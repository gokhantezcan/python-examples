from Car import Car

class Convertible(Car):
    def horn(self):
        print("bip bip")

    def get_info(self):
        Car.get_info(self)
        print("Harike bir kabriyo arabayım.")