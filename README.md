- Ячменев Иван михайлович
- ОЗИВТ-21-1-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |


знак "+" - задание выполнено

знак "-" - задание не выполнено

Работу проверили:
- к.э.н., доцент Панов М.А.


## Лабораторная работа №11

### 1) Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()

```python
numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_11/pic/lab/ex1.png)

### 2) Класс итератор с гибкой настройкой и удобными применением


```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count
    
if __name__ == "__main__":
    counter = CountDown(5)
    for i in counter:
        print(i)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_11/pic/lab/ex2.png)

### 3) Генератор списка


```python
a = [i ** 2 for i in range(1, 5)]

print(f"a - {a}")
for i in a:
    print(i)

print(f"iter(a) - {iter(a)}")
for i in a:
    print(i)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_11/pic/lab/ex3.png)

### 4) Выражения генераторы


```python
b = (i ** 2 for i in range(1, 5))
print(b)
print("first")
for i in b:
    print(i)

print("second")

for i in b:
    print(b)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_11/pic/lab/ex4.png)

### 5) Такой же счетчик, как и в первом задании, только это генератор и использует yield


```python
def countdown(count):
    while count >= 0:
        yield count
        count -= 1
    
if __name__ == "__main__":
    counter = countdown(5)
    for i in counter:
        print(i)
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_11/pic/lab/ex5.png)



## Самостоятельная работа №11


### 1) Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. 

Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.


```python
def fib(n):
    num = 1
    next_num = 1
    for _ in range(n):
        res = num + next_num
        num = next_num
        next_num = res
        yield res


print(list(fib(200)))
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_11/pic/praktika/ex1.png)

### 2) К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла


```python
def fib(n):
    num = 1
    next_num = 1
    with open("fib.txt", 'a+') as file:
        for _ in range(n):
            res = num + next_num
            num = next_num
            next_num = res
            file.write(f"{res}\n")


print(fib(200))
```

![ex1pic](https://github.com/RRelaxeDD/python_school_tasks/blob/theme_11/pic/praktika/ex2.png)
