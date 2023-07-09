# Планеты вращаются вокруг звезд по эллиптическим орбитам.

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(data := list(filter(lambda x: x[0] != x[1], orbits)))
# print(list := list(map(lambda x: x[0]*x[1]*3.14, data)))
# print(orbits[list.index(max(list))])
# orbits = [1, 2, 3, 4, 5, 6, 7, 89]
# print(data := list(map(lambda x: x[0]*x[0], orbits)))

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.

# def same_by(characteristic, item):
#     return len(item) == len(list(filter(characteristic, item)))


# list_1 = [2, 3, 4, 5, 6, 7, 8, 9]
# print(same_by(lambda x: x > 1, list_1))

# def same_by(characteristic, objects):
#     return len(set(map(characteristic, objects))) < 2


# list_1 = [2, 4, 6, 8]
# print(same_by(lambda x: x * 0, list_1))
