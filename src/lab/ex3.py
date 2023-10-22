class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"driving the {self.make} {self.model}")

class ElecricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"charging the {self.make} {self.model} with {self.battery_capacity} kwh")


    
my_car = ElecricCar("Toyota", "centry", 75)
my_car.drive()
my_car.charge()