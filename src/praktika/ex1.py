user_input = input("Ender array of numbers splitted by space:\n")

user_tuple = tuple(int(i) for i in user_input.split(" "))
print(user_tuple)
