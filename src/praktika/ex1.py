from pprint import pprint
with open("text_for_ex10.txt", 'r', encoding="utf8") as file:
    data = file.read()

words = data.lower().split(" ")
values_dict = {}
for i in words:
    if i in values_dict:
        values_dict[i] += 1
    else:
        values_dict[i] = 1

most_frequent_word = ""
most_freqent_count = 0

for i in values_dict:
    if values_dict[i] > most_freqent_count:
        most_frequent_word = i
        most_freqent_count = values_dict[i]

print(f"most frequent word: {most_frequent_word}, {most_freqent_count}")
