

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


## Лабораторная работа №7

### 1) Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.


![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex1.png)

### 2) Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().


```python
f = open("input.txt", "r")
print(f.readline())
f.close()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex2.png)

### 3) Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().


```python
f = open("input.txt", "r")
print(f.readlines())
f.close()
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex3.png)

### 4) Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().


```python
with open("input.txt", "r") as file:
    print(file.readlines())
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex4.png)

### 5) Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().


```python
with open("input.txt", "r") as file:
    for i in file.readlines():
        print(i)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex5.png)

### 6) Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.


```python
with open("input.txt", "a+") as file:
    file.write("\nsome new line")

with open("input.txt", 'r') as file:
    print(file.read())
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex6.png)

### 7) Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.


```python
lines = ["one", "two", "three"]
with open("input.txt", "w") as file:
    for i in lines:
        file.write(f"cycle run {i}")
    print("done")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex7.png)

### 8) Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).


```python
import os

def print_docs(direct):
    all_files = os.walk(direct)
    for catalog in all_files:
        print(f"dir {catalog[0]} contains:")
    print(f"dirs: {', '.join([folder for folder in catalog[1]])}")
    print(f"files: {', '.join([file for file in catalog[2]])}")
    print("-" * 20)

print_docs(".")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex8.png)

### 9) Документ «input.txt» содержит следующий текст:

```
Приветствие 
Спасибо 
Извините 
Пожалуйста 
До свидания 
Ты готов? 
Как дела? 
С днем рождения! 
Удача! 
Я тебя люблю.
```

Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). 

```python
def longest_words(file):
    with open(file, encoding="utf8") as file:
        words = file.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words("input2.txt"))
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex9.png)

### 10) Требуется создать csv-файл «rows_300.csv» со следующими столбцами:

- No - номер по порядку (от 1 до 300)
- Секунда – текущая секунда на вашем ПК;
- Микросекунда – текущая миллисекунда на часах

Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open("rows_300.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["#", "second", "milisecond"])
    for line in range(1, 301):
        writer.writerow(
            [
                line,
                datetime.datetime.now().second,
                datetime.datetime.now().microsecond
            ]
        )
        time.sleep(0.01)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/lab/ex10.png)

## Самостоятельная работа №7


### 1) Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.


```python
from pprint import pprint
with open("text_for_ex10.txt", 'r', encoding="utf8") as file:
    data = file.read()

words = data.lower().split(" ")
values_dict = {}
for i in words:
    if i in values_dict:
        values_dict[i] += 1
    else:
        values_dict[i] = 1

most_frequent_word = ""
most_freqent_count = 0

for i in values_dict:
    if values_dict[i] > most_freqent_count:
        most_frequent_word = i
        most_freqent_count = values_dict[i]

print(f"most frequent word: {most_frequent_word}, {most_freqent_count}")

```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/praktika/ex1.png)

### 2) У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль.  Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.


```python
import csv

user_input = int(input("1 - ввести данные\n2 - вывести информацию\n3 - сделать файл с таблицей\ninput: "))

if user_input == 1:

    value = float(input("введите цену: "))
    info = input("введите описание: ")
    with open("csv_for_pex2.csv", 'a+') as file:
        cursor = csv.writer(file)
        cursor.writerow([value, info])

elif user_input == 2:

    with open("csv_for_pex2.csv", 'r') as file:
        data = csv.reader(file)
        wasted_sum = sum([float(i[0]) for i in [i for i in data][1:]])
        print(f"all time wasted_money: {wasted_sum}")

elif user_input == 3:
    with open("csv_for_pex2.csv", 'w') as file:
        cursor = csv.writer(file)
        cursor.writerow(["price", "info"])
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/praktika/ex2.png)

### 3) Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

Текст в файле:

```
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated.
```

Ожидаемый результат:

```
Input file contains: 
108 letters 
20 words 
4 lines
```

```python
with open("text_for_pex3.txt", 'r') as file:
    data = file.read()

letters_count = sum((1 for i in data.lower() if i.isalpha()))
words_count = len(data.replace(".\n", " ").split(" "))
lines_count = len(data.split("\n"))

print(f"letters count: {letters_count}")
print(f"words count: {words_count}")
print(f"lines count: {lines_count}")
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/praktika/ex3.png)

### 4) Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на \*\*\*\*.

Запрещенные слова:

```
hello email python the exam wor is
```

Предложение для проверки:

```
Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
```

Ожидаемый результат:

```
*****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!
```

```python
# Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!

with open("text_for_pex4.text", 'r', encoding="utf8") as file:
    bad_words = file.read().lower().split(" ")

user_input = input("enter something: ").lower()

for i in bad_words:
    user_input = user_input.replace(i, "*"*len(i))

print(user_input)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/praktika/ex4.png)

### 5) Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.


```python
# написать рандомное количество слов в файл
import random
text = "sayhi "* random.randint(0, 100)
with open("text_for_pex5.text", 'w') as file:
    file.write(text)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_7/pic/praktika/ex5.png)
