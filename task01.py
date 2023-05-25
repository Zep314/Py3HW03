# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

def get_duplicate(in_list):  # Возвращаем список повторяющихся элементов входного списка
    v = set()
    return list(set([x for x in in_list if x in v or v.add(x)])) # Если элемент уже есть в set, то возвращаем его


if __name__ == '__main__':
    initial_list = [5, 2, 6, 8, 3, 5, 2, 1, 6, 2, 2, 5, 6, 7]
    print(f"Исходный список: {initial_list}")
    print(f"Список повторяющихся элементов: {get_duplicate(initial_list)}")

# Результат работы:
# /usr/bin/python3.10 /home/user/Work/Python/dz3/Py3HW03/task01.py
# Исходный список: [5, 2, 6, 8, 3, 5, 2, 1, 6, 2, 2, 5, 6, 7]
# Список повторяющихся элементов: [2, 5, 6]
#
# Process finished with exit code 0
