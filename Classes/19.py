# Write a Python class named Car with attributes like brand, model, and speed. Include a method to increase the speed.
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment

car = Car("Peugeot", "207", 190)
car.accelerate(20)
print(car.speed)
