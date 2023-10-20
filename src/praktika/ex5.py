# написать рандомное количество слов в файл
import random
text = "sayhi "* random.randint(0, 100)
with open("text_for_pex5.text", 'w') as file:
    file.write(text)