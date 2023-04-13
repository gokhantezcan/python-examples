
class Human:
    def __init__(self):
        print("Human")

class GRandPa1(Human):
    def __init__(self):
        print("GrandPa1")
        super().__init__()

class GRandPa2(Human):
    def __init__(self):
        print("GrandPa2")
        super().__init__()

class GRandMa1(Human):
    def __init__(self):
        print("GrandMa1")
        super().__init__()

class GRandMa2(Human):
    def __init__(self):
        print("GrandMa2")
        super().__init__()

class Father(GRandPa1, GRandMa1):
    def __init__(self):
        print("Father")
        super().__init__()

class Mother(GRandPa2, GRandMa2):
    def __init__(self):
        print("Mother")
        super().__init__()

class Child(Father, Mother):
    def __init__(self):
        print("Child")
        super().__init__()


child = Child()

