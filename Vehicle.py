class Vehicle:
    def __init__(self, licence_palte, color):
        self.licence_plate = licence_palte
        self.color = color
        self.velocity = 0

    def accelerate(self):
        self.velocity += 1

    def brake(self):
        self.velocity = 0

    def get_info(self):
        print(f"Ben bir aracım ve hızım {self.velocity}")
        print(f"Aracın plakası {self.licence_plate} dır ve rengi {self.color}")