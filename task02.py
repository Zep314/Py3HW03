# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из 
# википедии или из документации к языку. 

import string

BIG_TEXT_FILE = "C:\\Work\\python\\dz3\\Py3HW03\\big_text.txt "


def get_text_stat(in_text):  # Функция возвращает словарь слов с их частотой в тексте
    my_dict = {}
    for word in in_text.split(' '):
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))  # Сортировка
    return {my_key: my_dict[my_key] for my_key in list(my_dict.keys())[:10]}  # Возвращаем только 10 первых элементов


if __name__ == '__main__':
    with open(BIG_TEXT_FILE, 'r', encoding='UTF-8') as f:
        text = f.read()
        print(text)

        text = text.lower() \
            .replace("\n", " ") \
            .translate(str.maketrans('', '', string.punctuation)) \
            .replace('  ', ' ')

        print(f'\nЧастота : Слово')
        print(f'--------+------')
        for key, value in get_text_stat(text).items():
            print(f"{value:7} : {key}")

# Результат работы:
# C:\Work\python\dz3\Py3HW03\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW03/task02.py
# Python: В русском языке встречаются названия питон или пайтон - высокоуровневый язык
# программирования общего назначения с динамической строгой типизацией и автоматическим управлением
# памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества,
# а также на обеспечение переносимости написанных на нём программ. Язык является полностью
# объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью
# языка является выделение блоков кода пробельными отступами. Синтаксис ядра языка
# минималистичен, за счёт чего на практике редко возникает необходимость обращаться к
# документации. Сам же язык известен как интерпретируемый и используется в том числе для написания
# скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое
# потребление памяти написанных на нём программ по сравнению с аналогичным кодом,
# написанным на компилируемых языках, таких как C или C++.
#
# Python является мультипарадигменным языком программирования, поддерживающим императивное,
# процедурное, структурное, объектно-ориентированное программирование, метапрограммирование
# и функциональное программирование. Задачи обобщённого программирования решаются за счёт
# динамической типизации. Аспектно-ориентированное программирование частично поддерживается
# через декораторы, более полноценная поддержка обеспечивается дополнительными фреймворками.
# Такие методики как контрактное и логическое программирование можно реализовать с помощью
# библиотек или расширений. Основные архитектурные черты - динамическая типизация,
# автоматическое управление памятью, полная интроспекция, механизм обработки исключений,
# поддержка многопоточных вычислений с глобальной блокировкой интерпретатора, высокоуровневые
# структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь,
# могут объединяться в пакеты.
#
# Частота : Слово
# --------+------
#       7 : на
#       6 : и
#       5 : в
#       4 : с
#       4 : является
#       4 : программирование
#       3 : или
#       3 : язык
#       3 : программирования
#       3 : программ
#
# Process finished with exit code 0
