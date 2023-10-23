- Ячменев Иван михайлович
- ОЗИВТ-21-1-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.


## Лабораторная работа №10

### 1) Наверняка вы думаете, что декораторы – это какая-то бесполезная вещь, которая вам никогда не пригодится, но тут вдруг на паре по математике преподаватель просит всех посчитать число Фибоначчи для 100. 

Кто-то будет считать вручную (так точно не нужно), кто-то посчитает на калькуляторе, а кто-то подумает, что он самый крутой и напишет рекурсивную программу на Python и немного огорчится, потому что данная программа будет достаточно долго считаться, если ее просто так запускать. Но именно тут к вам на помощь приходят декораторы, например @lru_cache (он предназначен для решения задач динамическим программированием, если простыми словами, то этот декоратор запоминает промежуточные результаты и при рекурсивном вызове функции программа не будет считать одни и те же значения, а просто “возьмёт их из этого декоратора”). Вам нужно написать программу, которая будет считать числа Фибоначчи для 100 и запустить ее без этого декоратора и с ним, посмотреть на разницу во времени решения поставленной задачи. P.S. при запуске без декоратора можете долго не ждать, для наглядности хватит 10 секунд ожидания.

```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(fibonacci(100))
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/lab/ex1.png)

### 2) Илья пишет свой сайт и ему необходимо сделать минимальную проверку ввода данных пользователя при регистрации. Для этого он реализовал функцию, которая выводит данные пользователя на экран и решил, что будет проверять правильность введённых данных при помощи декоратора, но в этом ему потребовалась ваша помощь. Напишите декоратор для функции, который будет принимать все параметры вызываемой функции (имя, возраст) и проверять чтобы возраст был больше 0 и меньше 130. Причем заметьте, что неважно сколько пользователь введет данных на сайт к Илье, будут обрабатываться только первые 2 аргумента.


```python
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = "Недопустимый возраст"
        input_func(name, age)
    
    return output_func

@check
def personal_info(name, age):
    print(f"Name: {name} age: {age}")

if __name__ == "__main__":
    personal_info("Владимир", 38)
    personal_info("Александр", -5)
    personal_info("Петр", 130, 15, 48, 2)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/lab/ex2.png)

### 3) Вам понравилась идея Ильи с сайтом, и вы решили дальше работать вместе с ним. Но вот в вашем проекте появилась проблема, кто-то пытается сломать вашу функцию с получением данных для сайта. Эта функция работает только с данными integer, а какой-то недохакер пытается все сломать и вместо нужного типа данных отправляет string. Воспользуйтесь исключениями, чтобы неподходящий тип данных не ломал ваш сайт. Также дополнительно можете обернуть весь код функции в try/except/finally для того, чтобы программа вас оповестила о том, что выявлена какая-то ошибка или программа успешно выполнена.


```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    
    except Exception as ex:
        print(ex)
    
    finally:
        print("all info checked")

if __name__ == "__main__":
    data([1, 15, "hello", "i", "try", "to", "crash", "your", "site", "38", 45])
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/lab/ex3.png)

### 4) Продолжая работу над сайтом, вы решили написать собственное исключение, которое будет вызываться в случае, если в функцию проверки имени при регистрации передана строка длиннее десяти символов, а если имя имеет допустимую длину, то в консоль выводиться “Успешная регистрация”



```python
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException("Длина более 10 символов")
    else:
        print("Успешная регестрация")


if __name__ == "__main__":
    name = "12345678910"
    check_name(name)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/lab/ex4.png)

### 5) После запуска сайта вы поняли, что вам необходимо добавить логгер, для отслеживания его работы. Готовыми вариантами вы не захотели пользоваться, и поэтому решили создать очень простую пародию. Для этого создали две функции: \_\_init\_\_() (вызывается при создании класса декоратора в программе) и \_\_call\_\_() (вызывается при вызове декоратора). Создайте необходимый вам декоратор. Выведите все логи в консоль.


```python
class SiteChecker:

    def __init__(self, func):
        print("> class SiteChecker method __init__ launched")
        self.func = func
    
    def __call__(self):
        print(f"> checking before start {self.func.__name__}")
        self.func()
        print("> Checking safe turn off")

@SiteChecker
def site():
    print("site working")

if __name__ == "__main__":
    print(">> site started")
    site()
    print(">> site shutted down")

```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/lab/ex5.png)


## Самостоятельная работа №10


### 1) Вовочка решил заняться спортивным программированием на python, 

но для этого он должен знать за какое время выполняется его программа. Он решил, что для этого ему идеально подойдет декоратор для функции, который будет выяснять за какое время выполняется та или иная функция. Помогите Вовочке в его начинаниях и напишите такой декоратор. Подсказка: необходимо использовать модуль time Декоратор необходимо использовать для этой функции: 

```python
def fibonacci(): 
    fib1 = fib2 = 1 
 
    for i in range(2, 200): 
        fib1, fib2 = fib2, fib1 + fib2 
        print(fib2, end=' ') 
 
 
if __name__ == '__main__': 
    fibonacci()
```

Результатом вашей работы будет листинг кода и скриншот консоли, в котором будет выполненная функция Фибоначчи и время выполнения программы. Также на этом примере можете посмотреть, что решение задач через рекурсию не всегда является хорошей идеей. Поскольку решение Фибоначчи для 100 с использованием рекурсии и без динамического программирования решается более десяти секунд, а решение точно такой же задачи, но через цикл for еще и для 200, занимает меньше 1 секунды. 


```python
import time

def exec_time(func):

    def inner():
        start = time.time()
        func()
        end = time.time() - start
        print(f"\ntime of excecution is {end} seconds")
    
    return inner

@exec_time
def fibonacci(): 
    fib1 = fib2 = 1 
 
    for i in range(2, 200): 
        fib1, fib2 = fib2, fib1 + fib2 
        print(fib2, end=' ') 
 
 
if __name__ == '__main__': 
    fibonacci()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/praktika/ex1.png)

### 2) Посмотрев на Вовочку, вы также загорелись идеей спортивного программирования, начав тренировки вы узнали, что для решения некоторых задач необходимо считывать данные из файлов. Но через некоторое время вы столкнулись с проблемой что файлы бывают пустыми, и вы не получаете вводные данные для решения задачи. После этого вы решили не просто считывать данные из файла, а всю конструкцию оборачивать в исключения, чтобы избежать такой проблемы. Создайте пустой файл и файл, в котором есть какая-то информация. Напишите код программы. Если файл пустой, то, нужно вызвать исключение (“бросить исключение”) и вывести в консоль “файл пустой”, а если он не пустой, то вывести информацию из файла.


```python
def check_empty_file(func):

    def inner(file_path):

        with open(file_path, 'r') as file:
            data = file.readline()

        if not data: raise Exception("empty file")

        func(file_path)

    return inner

@check_empty_file
def do_file(path):
    with open(path, 'r') as file:
        print(f"--- file: {path}\n{file.read()}\n---\n")

do_file("not_empty_file.txt")
do_file("empty_file.txt")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/praktika/ex2.png)

### 3) Напишите функцию, которая будет складывать 2 и введенное пользователем число, но если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка “Неподходящий тип данных. Ожидалось число.”. Реализовать функционал программы необходимо через try/except и подобрать правильный тип исключения. Создавать собственное исключение нельзя. Проведите несколько тестов, в которых исключение вызывается и нет. Результатом выполнения задачи будет листинг кода и получившийся вывод в консоль


```python
try:
    user_input = int(input("enter a number: "))
    print(f"2 + {user_input} = {2 + user_input}")

except ValueError:
    raise ValueError
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/praktika/ex3.png)

### 4) Создайте собственный декоратор, который будет использоваться для двух любых вами придуманных функций. Декораторы, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс декоратора, две как-то связанными с ним функциями, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода. 


```python
class MyDecorators:

    @staticmethod
    def check_alpha(func):

        def inner(arg: str):
            
            for i in arg:
                if not i.isalpha():
                    print("not all chars are letter")
                    return
            func(arg)
        
        return inner
    
    @staticmethod
    def check_numbers(func):

        def inner(arg: str):

            for i in arg:
                if not i.isdigit():
                    print("not all chars are int")
                    return
            func(arg)    
        
        return inner



@MyDecorators.check_alpha
def print_if_all_letters(sentence):
    print(sentence)

@MyDecorators.check_numbers
def print_if_all_ints(sentence):
    print(int(sentence[0]))


print_if_all_letters("fnjasbdiuaoaiufiajw")
print_if_all_letters("fnjasbdiuaoaiufiajw1")

print_if_all_ints("385139740828")
print_if_all_ints("385139740828a")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/praktika/ex4.png)

### 5) Создайте собственное исключение, которое будет использоваться в двух любых фрагментах кода. Исключения, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс исключения, код к котором в двух местах используется это исключение, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода.


```python
class FirstChartNotIntException(Exception):
    pass

def some_function(arg):

    if not arg[0].isdigit():
        raise FirstChartNotIntException("first char must be int")
    
    print("all ok go next")

some_function("7361 7420 6869")
some_function("a7361 7420 6869")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_10/pic/praktika/ex5.png)
