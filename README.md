

- Ячменев Иван михайлович
- ОЗИВТ-21-1-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | - |
| Задание 2 | + | - |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.


## Лабораторная работа №4

### 1) Напишите функцию, которая выполняет любые арифметические действия и выводит результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    print(2 + 2)

if __name__ == "__main__":
    main()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex1.png)

### 2) Напишите функцию, которая выполняет любые арифметические действия, возвращает при помощи return значение в место, откуда вызывали функцию. Выведите результат в консоль. Вызовите функцию используя “точку входа”.


```python
def main():
    result = 2 + 2
    return result

if __name__ == "__main__":
    answer = main()
    print(answer)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex2.png)

### 3) Напишите функцию, в которую передаются два аргумента, над ними производится арифметическое действие, результат возвращается туда, откуда эту функцию вызывали. Выведите результат в консоль. Вызовите функцию в любом небольшом цикле. 


```python
def main(one, two):
    result = one + two
    return result

if __name__ == "__main__":
    x = 1
    y = 10
    answer = main(x, y)
    print(answer)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex3.png)

### 4) Напишите функцию, на вход которой подается какое-то изначальное неизвестное количество аргументов, над которыми будет производится арифметические действия. Для выполнения задания необходимо использовать кортеж “*args”. На скриншоте ниже приведен пример такой программы с комментариями.

```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"{one=}\n{two=}\n{three=}")
    return x + sum(args) / float(len(args))

if __name__ == "__main__":
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\n{result=}")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex4.png)

### 5) Напишите функцию, которая на вход получает кортеж “\*\*kwargs” и при помощи цикла выводит значения, поступившие в функцию. На скриншоте ниже указаны два варианта вызова функции с “**kwargs” и два варианта работы с данными, поступившими в эту функцию. Комментарии в коде и теоретическая часть помогут вам разобраться в этом нелегком аспекте. Вызовите функцию используя “точку входа”. 



```python
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    
    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    
if __name__ == "__main__":
    main(x=[1, 2, 3], y=[3, 3, 0], z=[2, 3, 0], q=[3, 3, 0], w=[3, 3, 0])
    print()
    main(**{"x":[1, 2, 3], "y":[3, 3, 0]})
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex5.png)

### 6) Напишите две функции. Первая – получает в виде параметра “\*\*kwargs”. Вторая считает среднее арифметическое из значений первой функции. Вызовите первую функцию используя “точку входа” и минимум 4 аргумента. 


```python
def main(**kwargs):

    for i, j in kwargs.items():
        print(f"{i}. mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == "__main__":
    main(x=[1, 2, 3], y=[3, 3, 0])
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex6.png)

### 7) Создайте дополнительный файл .py. Напишите в нем любую функцию, которая будет что угодно выводить в консоль, но не вызывайте ее в нем. Откройте файл main.py, импортируйте в него функцию из нового файла и при помощи “точки входа” вызовите эту функцию.


```python
from for_import import sayhi

if __name__ == "__main__":
    sayhi()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex7.png)

### 8) Напишите программу, которая будет выводить корень, синус, косинус полученного от пользователя числа.


```python
from math import *

def main():
    value = int(input("enter number: "))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == "__main__":
    main()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex8.png)

### 9) Напишите программу, которая будет рассчитывать какой день недели будет через n-нное количество дней, которые укажет пользователь.


```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"today {dt.today().date()}, "
        f"day of week - {dt.today().isoweekday()}"
    )
    n = int(input("enter number of days: "))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"через {n} дней будет{result.date()}, "
        f"day of week - {result.isoweekday()}"
    )

if __name__ == "__main__":
    main()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex9.png)

### 10) Напишите программу с использованием глобальных переменных, которая будет считать площадь треугольника или прямоугольника в зависимости от того, что выберет пользователь. Получение всей необходимой информации реализовать через input(), а подсчет площадей выполнить при помощи функций. Результатом программы будет число, равное площади, необходимой фигуры.


```python
global result

def rectangle():
    a = float(input("width: "))
    b = float(input("height: "))
    global result
    result = a + b

def triangle():
    a = float(input("base: "))
    h = float(input("height: "))
    global result
    result = 0.5 * a * h

figure = input("1 - прямоугольник\n2 - треугольник\ninput: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/lab/ex10.png)

## Самостоятельная работа №4


### 1) Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудь те, что функции комментируются по-особенному


```python
# импорт класса datetime из модуля datetime 
from datetime import datetime 
# импорт функции sqrt из модуля math
from math import sqrt 
 

def main(**kwargs):
    '''
    функция main которая принимает произвольное количество аргументов в виде пар ключ-значение
    
    проходит по каждому элементу словоря, делает вычисления и выводит результат
    '''

    # цикл for, проходится по каждому элементу словоря
    for key in kwargs.items():

        # делает вычисления из значений словоря
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) 
        # выводит результат вычисления
        print(result) 
 
# 'точка входа' в программу
if __name__ == '__main__':

    # получение текущего времени
    start_time = datetime.now() 

    # вызов функции main с аргументами
    main( 
        one=[10, 3], 
        two=[5, 4], 
        three=[15, 13], 
        four=[93, 53], 
        five=[133, 15] 
    )

    # получение времени выполнения программы
    time_costs = datetime.now() - start_time

    # вывод времени выполения программы 
    print(f"Время выполнения программы - {time_costs}") 
 


```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/praktika/ex1.png)

### 2) Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо использовать стандартную библиотеку random. Программу нужно написать, используя одну функцию и “точку входа”


```python
import random

def main():
    cube = random.randint(1, 6)
    print(f"{cube=}")
    if cube in (5, 6):
        print("you win")

    elif cube in (3, 4):
        main()


if __name__ == "__main__":
    main()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/praktika/ex2.png)

### 3) Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд. Программу нужно написать с использованием цикла. Подсказка: необходимо использовать модуль datetime и time, а также вам необходимо как-то “усыплять” программу на 1 секунду.


```python
from datetime import datetime
import time

for _ in range(5):
    print(datetime.now())
    time.sleep(1)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/praktika/ex3.png)

### 4) Напишите программу, которая считает среднее арифметическое от аргументов вызываемое функции, с условием того, что изначальное количество этих аргументов неизвестно. Программу необходимо реализовать используя одну функцию и “точку входа”.


```python
import random

def main(array):
    print(f"avg: {sum(array) / len(array)}")

if __name__ == "__main__":
    main([2, 2, 7, 1, 8, 3, 2, 3, 10, 7])
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/praktika/ex4.png)

### 5) Создайте два Python файла, в одном будет выполняться вычисление площади треугольника при помощи формулы Герона (необходимо реализовать через функцию), а во втором будет происходить взаимодействие с пользователем (получение всей необходимой информации и вывод результатов). Напишите эту программу и выведите в консоль полученную площадь.


```python
# geron.py

def s_triangle(x, y, z):
    '''
    x, y, z - стороны треугольника

    возвращает площадь треугольника по формуле Герона
    '''
    p = (x + y + z) / 2
    s = (p * (p - x) * (p - y) * (p - z)) ** 0.5
    return s
```


```python
# ex5.py

import geron

side1 = float(input("Введите длину стороны 1: "))
side2 = float(input("Введите длину стороны 2: "))
side3 = float(input("Введите длину стороны 3: "))

result = geron.s_triangle(
    side1,
    side2,
    side3
)
print(f"площадь треугольника: {result}")
```



![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_4/pic/praktika/ex5.png)