class Car:
    def __init__(self, make, model):
        self.make = make
        self._model = model
    
    def drive(self):
        print(f"driving the {self.make} {self._model}")

my_car = Car("Toyota", "centry")
print(my_car._model)
print(my_car.drive())