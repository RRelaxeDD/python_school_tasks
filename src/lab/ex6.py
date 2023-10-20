with open("input.txt", "a+") as file:
    file.write("\nsome new line")

with open("input.txt", 'r') as file:
    print(file.read())