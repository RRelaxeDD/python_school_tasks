- Ячменев Иван михайлович
- ОЗИВТ-21-1-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено

знак "-" - задание не выполнено

Работу проверили:
- к.э.н., доцент Панов М.А.


## Лабораторная работа №8

### 1) Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
my_car = Car("Toyota", "centry")
```

### 2) Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.


```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print(f"driving the {self.make} {self.model}")

    
my_car = Car("Toyota", "centry")
my_car.drive()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/lab/ex2.png)

### 3) Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.


```python
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
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/lab/ex3.png)

### 4) Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.


```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self._model = model
    
    def drive(self):
        print(f"driving the {self.make} {self._model}")

my_car = Car("Toyota", "centry")
print(my_car._model)
print(my_car.drive())
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/lab/ex4.png)

### 5) Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.


```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(10, 2), Circle(3)]
for shape in shapes:
    print(shape.area())
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/lab/ex5.png)


## Самостоятельная работа №8


### 1) Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
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
```


### 2) Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
class Phone:

    def __init__(self, model_name, price, company, battery_capacity, processor, camera):
        self.model_name = model_name
        self.price = price
        self.company = company
        self.battery_capacity = battery_capacity
        self.processor = processor
        self.camera = camera
    
    def print_info(self):
        print(f"\nmodel name: {self.model_name}\n"
              f"price: {self.price}\n"
              f"company: {self.company}\n"
              f"battery capacity: {self.battery_capacity}\n"
              f"processor: {self.processor}\n"
              f"camera: {self.camera}")

phone = Phone(
    "new cool phone ultra max pro elete exlusive limited edition milion",
    9999,
    "best company",
    10000,
    "p10milion",
    1000
)

phone.print_info()

```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/praktika/ex2.png)

### 3) Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
class Phone:

    def __init__(self, model_name, price, company, battery_capacity, processor, camera):
        self.model_name = model_name
        self.price = price
        self.company = company
        self.battery_capacity = battery_capacity
        self.processor = processor
        self.camera = camera
    
    def print_info(self):
        print(f"\nmodel name: {self.model_name}\n"
              f"price: {self.price}\n"
              f"company: {self.company}\n"
              f"battery capacity: {self.battery_capacity}\n"
              f"processor: {self.processor}\n"
              f"camera: {self.camera}")

class BestCompanyPhone(Phone):

    def __init__(self, model_name, price, company, battery_capacity, processor, camera, best_servies: bool, factory: int):
        super().__init__(model_name, price, company, battery_capacity, processor, camera)
        self.best_servies = best_servies
        self.factory = factory
    
    def print_info(self):
        print(f"\nBestCompanyPhone\n"
              f"model name: {self.model_name}\n"
              f"price: {self.price}\n"
              f"company: {self.company}\n"
              f"battery capacity: {self.battery_capacity}\n"
              f"processor: {self.processor}\n"
              f"camera: {self.camera}\n"
              f"best servies: {self.best_servies}\n"
              f"factory number: {self.factory}")

phone = BestCompanyPhone(
    "new cool phone ultra max pro elete exlusive limited edition milion",
    9999,
    "best company",
    10000,
    "p10milion",
    1000,
    True,
    1143
)

phone.print_info()

```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/praktika/ex3.png)

### 4) Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
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
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/praktika/ex4.png)

### 5) Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
class Phone:

    def is_foldable(self): pass

class RegularPhone(Phone):

    def __init__(self, name) -> None:
        self.name = name

    def is_foldable(self):
        return False

class FoldablePhone(Phone):

    def __init__(self, name) -> None:
        self.name = name

    def is_foldable(self):
        return True

phones = [RegularPhone("regular phone"), FoldablePhone("foldable phone")]

for i in phones:
    print(i.is_foldable())
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_8/pic/praktika/ex5.png)