# define parent class
class Vehicle:
    def __init__(self, regno, color):
        self.color = color
        self.regno = regno

# define child class


class Car(Vehicle):
    def __init__(self, regno, color):
        Vehicle.__init__(self, regno, color)

    def getType(self):
        return "Car"
