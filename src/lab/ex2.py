class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"driving the {self.make} {self.model}")

    
my_car = Car("Toyota", "centry")
my_car.drive()