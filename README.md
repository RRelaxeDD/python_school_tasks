# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнил(а):
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

## Лабораторная работа №2
### 1) Выведите в консоль три строки. Первая – любое число. Вторая – любое число в виде строки. Третья – любое число с плавающей точкой.

```python
print(123)
print('123')
print(1.23)
```

### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex1.png)

## Выводы

В данном коде выводятся три строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(123)`: Выводится целое число 123. Это число не взаимодействует со строковыми операциями и выводится как есть.

2. `print('123')`: Выводится строка '123', так как она заключена в одинарные кавычки. В этом случае это текстовая строка, а не число.

3. `print(1.23)`: Выводится число с плавающей точкой 1.23. Так же, как и в первом случае, оно выводится как числовое значение.

### 2) Выведите в консоль три строки. Первая – результат сложения или вычитания минимум двух переменных типа int. Вторая – результат сложения или вычитания минимум двух переменных типа float. Третья – результат сложения или вычитания минимум двух переменных типа int и float.

```python
print(1823 - 486)
print(5.1 - 8.27)
print(3 + 7.04 + 1 + 2.33)
```

### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex2.png)
 
 
### 3) Выведите в консоль три строки. Первая – обычная строка. Вторая – F строка с использованием заранее объявленной переменной. Третья – сложите две или более строк в одну.

```python
print("Привет, Мир!")

world = "World"
print(f"Hello {world}")

one = "Hello, "
two = "World!"
print(one + two)
```


### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex3.png)

### 4) Выведите в консоль три строки. Первая – трансформация любого типа переменной в bool. Вторая – трансформация любого типа переменной в float или int. Третья – трансформация любого типа переменной в str. 
 
```python
one = "hello"
print(bool(one))
two = 142
print(float(two))
three = None
print(str(three))
```


### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex4.png)
 
### 5) Присвойте трем переменным различные значения, воспользовавшись функцией input() 

```python
one = input("one: ")
two = input("two: ")
three = input("three: ")
print(one, two, three)
```


### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex5.png)

### 6) Создайте две любые числовые переменные и выполните над ними несколько математических операций: возведение в степень, обычное деление, целочисленное деление, нахождение остатка от деления. При желании вы можете проверить как работают эти вычисления с разными типами данных, например, сначала создать две переменные int, затем создать две переменные float и наконец создать переменные типа int и float и провести над ними операции, прописанные выше.

```python
a = 12
b = 5
print(f"Maging a square: {a**b}")
print(f"Division {a/b}")
print(f"целочисленное деление: {a//b}")
print(f"нахождение остатка от деления: {a%b}")
```


### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex6.png)
 
 
### 7) Создайте любую строковую переменную и произведите над ней математическое действие умножение на любое число. 

```python
line = "hello"
print(line * 6)
```


### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex7.png)


### 8) Посчитайте сколько раз символ ‘o’ встречается в строке ‘Hello World’. 

```python
sentenct = "hello world"
print(sentenct.count("o"))
```


### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex8.png)
 
### 9) Напишите предложение ‘Hello World’ в две строки. Написанная программа должна занимать одну строку в редакторе кода. 

```python
print("hello\nworld")
```


### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex9.png)
 
### 10) Из предложения ‘Hello World’ выведите в консоль только 2 символ, а затем выведите слово ‘Hello’ 

```python
sentence = "hello world"
print(sentence[1])
print(sentence[:5])
```

### Результат.
![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/lab/ex10.png)

## Самостоятельная работа №2
### 1) Выведите в консоль булевую переменную False, не используя слово False в строке или изначально присвоенную булевую переменную. Программа должна занимать не более двух строк редактора кода.

```python
print(bool(0))
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex1.png)

### 2) Присвоить значения трем переменным и вывести их в консоль, используя только две строки редактора кода

```python
a, b, c = "hi", "im", "van"
print(a, b, c)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex2.png)

### 3) Реализуйте ввод данных в программу, через консоль, в виде только целых чисел (тип данных int). То есть при вводе буквенных символов в консоль, программа не должна работать. Программа должна занимать не более двух строк редактора кода.

```python
user_input = int(input("enter a number: "))
print(user_input)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex3.png)

### 4) Создайте только одну строковую переменную. Длина строки должна не превышать 5 символов. На выходе мы должны получить строку длиной не менее 16 символов. Программа должна занимать не более двух строк редактора кода.


```python
word = "sayhi"
print(word*10)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex4.png)

### 5) Создайте три переменные: день (тип данных - числовой), месяц (тип данных - строка), год (тип данных - числовой) и выведите в консоль текущую дату в формате: “Сегодня день месяц год. Всего хорошего!” используя F строку и оператор end внутри print(), в котором вы должны написать фразу “Всего хорошего!”. Программа должна занимать не более двух строк редактора кода.

```python
day, month, year = 1, "january", 2023
print(f"Сегодня {day} {month} {year}. ", end="Всего хорошего!")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex5.png)

### 6) В предложении ‘Hello World’ вставьте ‘my’ между двумя словами. Выведите полученное предложение в консоль в одну строку. Программа должна занимать не более двух строк редактора кода.

```python
print("Hello World".replace(" ", " my "))
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex6.png)

### 7) Узнайте длину предложения ‘Hello World’, результат выведите в консоль. Программа должна занимать не более двух строк редактора кода.


```python
print(len("Hello World"))
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex7.png)

### 8) Переведите предложение ‘HELLO WORLD’ в нижний регистр. Программа должна занимать не более двух строк редактора кода.


```python
print("HELLO WORLD".lower())
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex8.png)

### 9) Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть связанна со взаимодействием с числовыми значениями.


```python
# сделать лист из строки и вывести его
word = [i for i in "sayhi"]
print(word)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex9.png)

### 10) Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть связанна со взаимодействием с числовыми значениями.


```python
# сделать строку в верхний регистр
print("sayhi".upper())
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_2/pic/praktika/ex10.png)