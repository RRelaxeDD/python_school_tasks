- Ячменев Иван михайлович
- ОЗИВТ-21-1-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |


знак "+" - задание выполнено

знак "-" - задание не выполнено

Работу проверили:
- к.э.н., доцент Панов М.А.


## Лабораторная работа №9

### 1) Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте  класс,  указав  в  свойствах  только  имя.  Дальше  создайте функцию \_\_init\_\_(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав  атрибут,  который  не  указан  в  вашем  классе,  например, попробуйте вызвать фамилию.

```python
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
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_9/pic/lab/ex1.png)

### 2) Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет  определяться  изменили  ли  состав  мороженого  или  нет.  В  этом классе  реализуйте  метод,  выводящий  на  печать  «Мороженое  с {ТОППИНГ}»  в  случае  наличия  добавки,  а  иначе  отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.


```python
class Icecream:

    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    
    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print("Обычное мороженое")
    
icecream = Icecream()
icecream.composition()

icecream = Icecream("укроп")
icecream.composition()

icecream = Icecream(6)
icecream.composition()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_9/pic/lab/ex2.png)

### 3) Петя – начинающий программист и на занятиях ему сказали реализовать икапсу...что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу...что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также  вас  необходимо  объяснить  Пете  почему  на  скриншоте  ниже  в консоли выводится ошибка.


```python
class MyClass:


    def __init__(self, value):
        self._value = value
    
    def set_value(self, value):
        self._value = value
    
    def get_value(self):
        return self._value

    def del_value(self):
        del self._value
    
    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())

obj.set_value(45)
print(obj.get_value())

obj.set_value(100)
print(obj.get_value())

obj.del_value()
print(obj.get_value())


```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_9/pic/lab/ex3.png)

### 4) Вам  прекрасно  известно,  что  кошки  и  собаки  являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования”  объяснить  компьютеру  что  кошки  и  собаки  –  это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга. 


```python
class Mammal:
    className = "Mammal"

class Dog(Mammal):
    species = "canie"
    sounds = "wow"

class Cat(Mammal):
    species = "feline"
    sounds = "meow"

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")

cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_9/pic/lab/ex4.png)

### 5) На  разных  языках  здороваются  по-разному,  но  суть  остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть  первого  предложения  задачи.  Для  этого  мы  можем  выбрать  два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих  языках.  А  также  напишем  функцию,  которая  будет  выводить информацию о том, как на этих языках здороваются.  Заметьте,  что  для  решения  поставленной  задачи  мы  использовали декоратор  @staticmethod,  поскольку  нам  не  нужны  обязательные параметры-ссылки вроде self.


```python
class Russian:

    @staticmethod
    def greeting():
        print("привет")
    
class English:
    
    @staticmethod
    def greeting():
        print("hello")


def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)

john = English()
greet(john)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_9/pic/lab/ex5.png)


## Самостоятельная работа №9


### 1) Задание Садовник и помидоры.

Классовая структура: 

Есть Помидор со следующими характеристиками: 
- Индекс 
- Стадия созревания (стадии: отсутствует, цветение, зеленый, красный) 

Помидор может: 
- Расти (переходить на следующую стадию созревания) 
- Предоставлять информацию о своей зрелости 
 
Есть Куст с помидорами, который: 
- Содержит список томатов, которые на нем растут 

А также может: 
- Расти вместе с томатами 
- Предоставлять информацию о зрелости всех томатов 
- Предоставлять урожай 

И также есть Садовник, который имеет: 
- Имя 
- Растение, за которым он ухаживает 

Он может: 
- Ухаживать за растением 
- Собирать с него урожай 
 
Задание:

Класс Tomato: 

1) Создайте класс Tomato 
2) Создайте статическое свойство states, которое будет содержать все 
стадии созревания помидора 
3) Создайте метод __init__(), внутри которого будут определены два 
динамических свойства: _index (передается параметром) и _state Михаил А. Панов
(принимает первое значение из словаря states). После написания 
этого блока кода в комментарии к нему укажите какими являются 
эти два свойства 
4) Создайте метод grow(), который будет переводить томат на 
следующую стадию созревания 
5) Создайте метод is_ripe(), который будет проверять, что томат созрел 

Класс TomatoBush: 
1) Создайте класс TomatoBush 
2) Определите метод __init__(), который будет принимать в качестве 
параметра количество томатов и на его основе будет создавать 
список объектов класса Tomato. Данный список будет храниться 
внутри динамического свойства tomatoes 
3) Создайте метод grow_all(), который будет переводить все объекты 
из списка томатов на следующий этап созревания 
4) Создайте метод all_are_ripe(), который будет возвращать True, если 
все томаты из списка стали спелыми. 
5) Создайте метод give_away_all(), который будет чистить список 
томатов после сбора урожая 

Класс Gardener: 
1) Создайте класс Gardener 
2) Создайте метод __init__(), внутри которого будут определены два 
динамических свойства: name (передается параметром, является 
публичным) и _plant (принимает объект класса TomatoBush). После 
написания этого блока кода в комментарии к нему укажите какими 
являются эти два свойства 
3) Создайте метод work(), который заставляет садовника работать, что 
позволяет растению становиться более зрелым 
4) Создайте метод harvest(), который проверяет, все ли плоды созрели. 
Если все, то садовник собирает урожай. Если нет, то метод печатает 
предупреждение 
5) Создайте статический метод knowledge_base(), который выведет в 
консоль справку по садоводству 

Тесты: 
1) Вызовите справку по садоводству 
2) Создайте объекты классов TomatoBush и Gardener 
3) Используя объект класса Gardener, поухаживайте за кустом с 
помидорами 
4) Попробуйте собрать урожай, когда томаты еще не дозрели. 
Продолжайте ухаживать за ними Михаил А. Панов
5) Соберите урожай 
Результатом работы вашей программы будет листинг кода с подробными 
комментариями и скриншоты выполенния всех тестов.

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_9/pic/praktika/ex1.png)

```python
class Tomato:

    states = ["нету", "цветение", "зеленый", "красный"]
    state_index = 0

    def __init__(self, index):
        """
        make dynamic properties:
        _index: int
        _state: str
        """
        self._index = index
        self._state = self.states[self.state_index]

    def grow(self):
        """
        change state of tomato
        """
        self.state_index += 1
        self._state = self.states[self.state_index]
    
    def is_ripe(self):
        """
        return True if tomato state is last state
        """
        return self._state == self.states[-1]

class TomatoBush:

    def __init__(self, number_of_tomatoes):
        """
        make tomato bush by specifying amount of tomatoes on bush
        """
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    def grow_all(self):
        """
        change state of all tomatoes on bush
        """
        for i in self.tomatoes:
            i.grow()

    
    def all_are_ripe(self):
        """
        return true if bush is ready to harvest
        """
        return self.tomatoes[0].is_ripe()


    def give_away_all(self):
        """
        return tomatoes and delete them from class
        """
        tomatoes = self.tomatoes
        del self.tomatoes
        return tomatoes

class Gardener:

    plant_harvested = 0

    def __init__(self, name, plant: TomatoBush):
        """
        make gardener with name and given tomato bush
        """
        self.name = name
        self._plant = plant

    def work(self):
        """
        make bush growing
        """
        print("working....")
        self._plant.grow_all()

    
    def harvest(self):
        """
        if plant ready to harvest, make harvest and return tomatoes
        """

        if self._plant.all_are_ripe():
            print("harvesting")
            self.plant_harvested += 1
            return self._plant.give_away_all()
        print("plant not ready yet")
    
    def knowledge_base(self):
        """
        print info about gardener
        """
        print(f"\ngardener name: {self.name}\nharvested: {self.plant_harvested}")
    
tomato_bush = TomatoBush(10)

gardener = Gardener("bob", tomato_bush)

gardener.knowledge_base()

gardener.work()

gardener.harvest()

gardener.work()

gardener.work()

tomatoes = gardener.harvest()

print(tomatoes[1]._index)

gardener.knowledge_base()
```