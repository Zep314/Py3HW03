# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из 
# википедии или из документации к языку. 

import string

BIG_TEXT_FILE = "/home/dima/Work/Python/dz3/Py3HW03/big_text.txt"

def get_text_stat(text):
    my_dict = {}
    for word in text.split(' '):
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse = True))
    keys = list(my_dict.keys())
    return keys[:10]

if __name__ == '__main__':
    with open(BIG_TEXT_FILE, 'r', encoding='UTF-8') as f:
        text = f.read()
        print(text)

        text = text.lower()\
                   .replace("\n", " ")\
                   .translate(str.maketrans('', '', string.punctuation))
        print(get_text_stat(text))
