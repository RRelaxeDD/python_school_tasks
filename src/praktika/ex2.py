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