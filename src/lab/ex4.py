def personal_info(name, age, company="unnamed"):
    print(f"Name: {name} age: {age} company: {company}")

tom = ("grigory", 22)
personal_info(*tom)

bob = ("girgory", 41, "yandex")
personal_info(*bob)
