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