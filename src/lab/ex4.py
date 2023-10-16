numbers = [1, 3, 4, 6, 8, 9, 15, 16,73, 321, 322]
value = int(input("enter number: "))
if value in numbers:
    if value % 2 == 0:
        print("переменная четная и есть в массиве numbers")
    else:
        print("переменная нечетная и есть в массиве numbers")
else:
    print(f"переменной нет в массиве numbers и она равна {value}")