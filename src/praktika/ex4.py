# Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!

with open("text_for_pex4.text", 'r', encoding="utf8") as file:
    bad_words = file.read().lower().split(" ")

user_input = input("enter something: ").lower()

for i in bad_words:
    user_input = user_input.replace(i, "*"*len(i))

print(user_input)