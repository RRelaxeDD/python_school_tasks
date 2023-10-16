even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True

if flag is True:
    print("в массиве есть нечетное число")
else:
    print("в массиве все числа четные")