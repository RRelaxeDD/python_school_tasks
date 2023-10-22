class Phone:

    def __init__(self, model_name, price, company, battery_capacity, processor, camera):
        self.model_name = model_name
        self.price = price
        self.company = company
        self.battery_capacity = battery_capacity
        self.processor = processor
        self.camera = camera

phone = Phone(
    "new cool phone ultra max pro elete exlusive limited edition milion",
    9999,
    "best company",
    10000,
    "p10milion",
    1000
)