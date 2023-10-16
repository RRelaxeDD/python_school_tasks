

- Ячменев Иван михайлович
- ОЗИВТ-21-1-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | + |
| Задание 7 | + | + |
| Задание 8 | + | + |
| Задание 9 | + | + |
| Задание 10 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.


## Лабораторная работа №3

### 1) Создайте две переменные, значение которых будете вводить через консоль. Также составьте условие, в котором созданные ранее переменные будут сравниваться, если условие выполняется, то выведете в консоль «Выполняется», если нет, то «Не выполняется».

```python
one = int(input("enter first num: "))
two = int(input("enter second num: "))
if one >= two:
    print("выполняется")
else:
    print("не выполняется")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex1.png)

### 2) Напишите программу, которая будет определять значения переменной меньше 0, больше 0 и меньше 10 или больше 10. Это нужно реализовать при помощи одной переменной, значение которой будет вводится через консоль, а также при помощи конструкций if, elif, else.

```python
one = int(input("enter first num: "))
if one < 0:
    print("переменная меньше 0")
elif 0 < one < 10:
    print("переменная больше 0 и меньше 10")
else:
    print("переменная больше 10")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex2.png)

### 3) Напишите программу, в которой будет проверяться есть ли переменная в указанном массиве используя логический оператор in. Самостоятельно посмотрите, как работает программа со значениями которых нет в массиве numbers. 
 

```python
numbers = [1, 3, 4, 6, 8, 9]
value = int(input("enter num: "))
if value in numbers:
    print("value in array")
else:
    print("value not in array")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex3.png)

### 4)Напишите программу, которая будет определять находится ли переменная в указанном массиве и если да, то проверьте четная она или нет. Самостоятельно протестируйте данную программу с разными значениями переменной value. 

```python
numbers = [1, 3, 4, 6, 8, 9, 15, 16,73, 321, 322]
value = int(input("enter number: "))
if value in numbers:
    if value % 2 == 0:
        print("переменная четная и есть в массиве numbers")
    else:
        print("переменная нечетная и есть в массиве numbers")
else:
    print(f"переменной нет в массиве numbers и она равна {value}")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex4.png)

### 5) Напишите программу, в которой циклом for значения переменной i будут меняться от 0 до 10 и посмотрите, как разные виды сравнений и операций работают в цикле. Михаил А. Панов


```python
for i in range(10):
    print(f"{i=}")
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print("переменная равна 2 или 3")
    elif i in [4, 5, 6]:
        print("переменная равна 4, 5 или 6")
    else:
        break
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex5.png)

### 6) Напишите программу, в которой при помощи цикла for определяется есть ли переменная value в строке string и посмотрите, как работает оператор else для циклов. Самостоятельно посмотрите, что выведет программа, если значение переменной value оказалось в строке string. Определять индекс буквы не обязательно, но если вы хотите, то это делается при помощи строки: index = string.find(value) Вы берете название переменной, в которой вы хотите что-то найти, затем применяете встроенный метод find() и в нем указываете то, что вам нужно найти. Данная строка вернет индекс искомого объекта. 

```python
string = "привет всем изучающим python!"
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"буква '{value}' есть в строке под {index} индексом")
        break
else:
    print(f"буквы '{value}' нет в указанной строке")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex6.png)

### 7) Напишите программу, в которой вы наглядно посмотрите, как работает цикл for проходя в обратном порядке, то есть, к примеру не от 0 до 10, а от 10 до 0. В уже готовой программе показано вычитание из 100, а вам во время реализации программы будет необходимо придумать свой вариант применения обратного цикла


```python
value = 100
for i in range(10, -1, -1):
    value -= 1
    print(i, value)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex7.png)

### 8) Напишите программу используя цикл while, внутри которого есть какие-либо проверки.

```python
value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1:
        value *= 5
    else:
        value -= 5
    print(value)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex8.png)

### 9) Напишите программу с использованием вложенных циклов и одной проверкой внутри них. Самое главное, не забудьте, что нельзя использовать одинаковые имена итерируемых переменных, когда вы используете вложенные циклы.


```python
value = 0
for i in range(10):
    for j in range(10):
        if i != j:
            value += j
        else:
            pass
print(value)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex9.png)

### 10) Напишите программу с использованием flag, которое будет определять есть ли нечетное число в массиве. В данной задаче flag выступает в роли индикатора встречи нечетного числа в исходном массиве, четных чисел.

```python
even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True

if flag is True:
    print("в массиве есть нечетное число")
else:
    print("в массиве все числа четные")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/lab/ex10.png)

## Самостоятельная работа №3


### 1) Напишите программу, которая преобразует 1 в 31. Для выполнения поставленной задачи необходимо обязательно и только один раз использовать:
- Цикл for 
- *= 5 
- += 1 
Никаких других действий или циклов использовать нельзя.

```python
for i in range(6, 7):
    i *= 5
    i += 1
print(f"{i=}")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/praktika/ex1.png)

### 2) Напишите программу, которая фразу «Hello World» выводит в обратном порядке, и каждая буква находится в одной строке консоли. При этом необходимо обязательно использовать любой цикл, а также программа должна занимать не более 3 строк в редакторе кода. 

```python
string = "Hello World"
for i in string[::-1]:
    print(i)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/praktika/ex2.png)

### 3) Напишите программу, на вход которой поступает значение из консоли, оно должно быть числовым и в диапазоне от 0 до 10 включительно (это необходимо учесть в программе). Если вводимое число не подходит по требованиям, то необходимо вывести оповещение об этом в консоль и остановить программу. Код должен вычислять в каком диапазоне находится полученное число. Нужно учитывать три диапазона: 
- от 0 до 3 включительно 
- от 3 до 6 
- от 6 до 10 включительно 

Результатом работы программы будет выведенный в консоль диапазон. 

Программа должна занимать не более 10 строчек в редакторе кода.

```python
user_input = int(input("enter number: "))
if not (0 <= user_input <= 10):
    print("число не подходит по условиям")
else:
    if user_input in range(0, 4):
        print("число в диапозоне от 0 до 3 включительно")
    elif user_input in range(3, 6):
        print("число в диапозоне от 3 до 6")
    elif user_input in range(6, 11):
        print("число в диапозоне от 6 до 10 включительно")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/praktika/ex3.png)

### 4) Манипулирование строками. Напишите программу на Python, которая принимает предложение (на английском) в качестве входных данных от пользователя. Выполните следующие операции и отобразите результаты: 

- Выведите длину предложения. 
- Переведите предложение в нижний регистр. 
- Подсчитайте количество гласных (a, e, i, o, u) в предложении. 
- Замените все слова "ugly" на "beauty". 
- Проверьте, начинается ли предложение с "The" и заканчивается ли на "end". 

Проверьте работу программы минимум на 3 предложениях, чтобы охватить проверку всех поставленных условий.

```python
# The ugly apple
# go to the end
# soad ieaiaio

user_input = input("enter a string: ")

print(f"{len(user_input)=}")

print(f"lower: {user_input.lower()}")

print(f"количество гласных: {sum([user_input.count(i) for i in ['a', 'e', 'i', 'o', 'u']])}")

print(f"ugly to beauty: {user_input.replace('ugly', 'beauty')}")

if user_input.startswith("The"):
    print("придлоежние начинается с 'The'")

elif user_input.endswith("end"):
    print("предложение заканичвается на 'end'")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/praktika/ex4.png)

### 5) Составьте программу, 
результатом которой будет данный вывод в консоль:

```
hello world
hello
hello world
hello
hello world
hello
hello world
hello
hello world
hello
hello world
```


Программу нужно составить из данных фрагментов кода:

```
counter = 0
values = [0, 2, 4, 6, 8, 10]
while counter != 10:
string = "hello"
if counter in values:
string = string + " world"
print(string)
counter += 1
memory = " world"
print(string + memory)
if values not in string:
while " world" not in string:
counter = 10
string = memory
string = 'world'
if counter > 7:
memory = string
if counter < 10:
print(memory)
memory = string
```
Строки кода можно использовать только один раз. Не обязательно использовать все строки кода.

```python
counter = 0
values = [0, 2, 4, 6, 8, 10]
while counter != 10:
    string = "hello"
    if counter in values:
        string = string + " world"
    print(string)
    counter += 1

memory = " world"
print(string + memory)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_3/pic/praktika/ex5.png)