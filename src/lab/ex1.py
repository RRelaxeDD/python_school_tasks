class Ivan:
    __slots__ = ["name"]

    def __init__(self, name):
        if name == "Иван":
            self.name = "Да, я Иван"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan("Алексей")
person2 = Ivan("Иван")
print(person1.name)
print(person2.name)

person2.shurname = "Петров"