def longest_words(file):
    with open(file, encoding="utf8") as file:
        words = file.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words("input2.txt"))