class Phone:

    def __init__(self, model_name, price, company, battery_capacity, processor, camera):
        self.model_name = model_name
        self.price = price
        self.company = company
        self.battery_capacity = battery_capacity
        self._processor = processor
        self.camera = camera
    
    def print_info(self):
        print(f"\nmodel name: {self.model_name}\n"
              f"price: {self.price}\n"
              f"company: {self.company}\n"
              f"battery capacity: {self.battery_capacity}\n"
              f"processor: {self._processor}\n"
              f"camera: {self.camera}")


phone = Phone(
    "new cool phone ultra max pro elete exlusive limited edition milion",
    9999,
    "best company",
    10000,
    "p10milion",
    1000,
    
)

print(phone._processor)

phone.print_info()
