class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.color} {self.brand} is starting...")

# Create object
my_car = Car("Toyota", "Red")
my_car.start()
