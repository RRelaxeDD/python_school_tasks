string = "привет всем изучающим python!"
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"буква '{value}' есть в строке под {index} индексом")
        break
else:
    print(f"буквы '{value}' нет в указанной строке")