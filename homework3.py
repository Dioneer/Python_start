# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = int(input('Введите размер списка:'))
# list_1 = []
# count = 0
# for i in range(n+1):
#     if i < n:
#         k = int(input('Введите натуральное число для заполнения массива:'))
#         list_1.append(k)
#     else:
#         x = int(input('Введите натуральное число для поиска:'))
# for i in list_1:
#     if (x == i):
#         count += 1
# print(count)

# Одной строкой, но надо в создании массива закоментировать else и все, что ниже
# print(list_1.count(int(input('Введите натуральное число для поиска:'))))


#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = int(input('Введите размер списка:'))
# list_1 = []
# result1 = 'нет большего ближнего числа,'
# result2 = 'нет меньшего ближнего числа'
# small_list = []
# big_list = []
# for i in range(n+1):
#     if i < n:
#         k = int(input('Введите натуральное число для заполнения массива:'))
#         list_1.append(k)
#     else:
#         x = int(input('Введите натуральное число для поиска:'))

# for i in range(len(list_1)):
#     if x <= list_1[i]:
#         big_list.append(list_1[i])
#     elif x > list_1[i]:
#         small_list.append(list_1[i])

# for i in range(len(big_list)):
#     result1 = big_list[0]
#     if result1 > big_list[i]:
#         result1 = big_list[i]

# for i in range(len(small_list)):
#     result2 = small_list[0]
#     if result2 < small_list[i]:
#         result2 = small_list[i]

# print(f'ближайшее большее/равное число = {result1},' if type(result1) is int else
#       result1, f'ближайшее меньшее число = {result2}' if type(result2) is int else result2)

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# list_dict = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, "А": 1, "J": 8, "X": 8, 'Q': 10, 'Z': 10, 'В': 1, 'Е': 1,
#              'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'Й': 4, ' Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10}

# word = input("Введи слово:").upper()
# count = 0
# for i in range(len(word)):
#     for j, k in list_dict.items():
#         if word[i] == j:
#             count += k
#             break
# print(count)
