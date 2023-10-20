with open("text_for_pex3.txt", 'r') as file:
    data = file.read()

letters_count = sum((1 for i in data.lower() if i.isalpha()))
words_count = len(data.replace(".\n", " ").split(" "))
lines_count = len(data.split("\n"))

print(f"letters count: {letters_count}")
print(f"words count: {words_count}")
print(f"lines count: {lines_count}")