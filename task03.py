# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

BACKPACK_CAPACITY = 2000  # Емкость рюкзака

dict_items = {'Одежда для сна': (300, 750),  # Список вещей
              'Нижнее белье': (500, 800),
              'Футболка': (400, 1000),
              'Рубашка с длинным руковам': (200, 500),
              'Носки': (200, 400),
              'Штаны': (200, 700),
              'Шорты': (300, 800),
              'Свитер': (200, 300),
              'Куртка': (100, 300),
              'Купальник': (200, 600),
              'Перчатки': (150, 200),
              'Шапка': (150, 300),
              'Ботинки': (250, 450),
              'Кроссовки': (250, 700),
              'Набор посуды': (150, 300),
              'Фляжка': (100, 200),
              'Предметы личной гигиены': (300, 700),
              'Солнцезащитный крем': (25, 100),
              'Солнечные очки': (30, 200),
              'Аптечка': (45, 250),
              'Полотенце': (175, 300),
              'Часы': (25, 400),
              'Фотоаппарат': (250, 400),
              'Спички': (20, 300),
              'Веревка': (30, 350),
              'Документы': (200, 400),
              'Деньги': (100, 800),
              'Телефон': (150, 250),
              }


def get_size_and_weight(local_dict_items):  # Возвращаем размер и вес предмета
    l_size = [local_dict_items[item][0] for item in local_dict_items]
    l_weight = [local_dict_items[item][1] for item in local_dict_items]
    return l_size, l_weight


def get_memtable(local_dict_items, backpack_capacity=BACKPACK_CAPACITY):  # Возвращаем таблицу мемоизации
    l_size, l_weight = get_size_and_weight(local_dict_items)
    n = len(l_weight)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    v = [[0 for _ in range(backpack_capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for a in range(backpack_capacity + 1):
            # базовый случай
            if i == 0 or a == 0:
                v[i][a] = 0

            # если размер предмета меньше веса столбца,
            # максимизируем значение суммарного веса
            elif l_size[i - 1] <= a:
                v[i][a] = max(l_weight[i - 1] + v[i - 1][a - l_size[i - 1]], v[i - 1][a])

            # если размер предмета больше размера столбца,
            # забираем значение ячейки (вес) из предыдущей строки
            else:
                v[i][a] = v[i - 1][a]
    return v, l_size, l_weight


def get_selected_items_list(local_dict_items, backpack_capacity=BACKPACK_CAPACITY):  # Возвращаем результат
    v, l_size, l_weight = get_memtable(local_dict_items)
    n = len(l_weight)
    res = v[n][backpack_capacity]  # начинаем с последнего элемента таблицы
    a = backpack_capacity  # начальный размер - максимальный
    items_list = []  # список размеров и весов

    for i in range(n, 0, -1):  # идём в обратном порядке
        if res <= 0:  # условие прерывания - собрали рюкзак
            break
        if res == v[i - 1][a]:  # ничего не делаем, двигаемся дальше
            continue
        else:
            # "забираем" предмет
            items_list.append((l_size[i - 1], l_weight[i - 1]))
            res -= l_weight[i - 1]  # отнимаем значение веса от общего веса
            a -= l_size[i - 1]  # отнимаем размер от общего размера

    selected_stuff = []

    # находим ключи исходного словаря - названия предметов
    for search in items_list:
        for my_key, l_weight in local_dict_items.items():
            if l_weight == search:
                selected_stuff.append(my_key)
    return selected_stuff


if __name__ == '__main__':
    print(f"Ёмкость рюкзака: {BACKPACK_CAPACITY}")
    print('Список всех вещей (Название: (Размер, Вес):')
    for key, value in dict_items.items():
        print(f"{key:10} : {value}")

    print('\nСписок вещей, которые влезли в рюкзак:')
    stuff = get_selected_items_list(dict_items)
    print(stuff)
    print(f"Всего занято места: {sum([dict_items[item][0] for item in stuff])}")
    print(f"Общий вес вещей в рюкзаке: {sum([dict_items[item][1] for item in stuff])}")
