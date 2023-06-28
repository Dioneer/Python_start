from random import randint
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# list1_len = int(input("Введите длину множества: "))
# list2_len = int(input("Введите длину множества: "))
# list_1 = []
# list_2 = []
# flag = True
# # ===================================== внутри располагаются простые циклы, но это не мой путь=)
# # test = set()
# # test2 = set()
# # while list1_len > len(test):
# #     number = randint(0, 20)
# #     test.add(number)
# # print(f'while {test}')
# # while list2_len > len(test2):
# #     number = randint(0, 20)
# #     test2.add(number)
# # print(f'while {test2}')
# # ============================================
# # цикл для первого списка
# for i in range(list1_len):
#     flag = True
#     number = randint(0, 20)
#     if number not in list_1:
#         list_1.append(number)
#     else:
#         while flag:
#             number = randint(0, 20)
#             if number not in list_1:
#                 list_1.append(number)
#                 flag = False
# print(list_1)

# # цикл для второго списка
# for i in range(list2_len):
#     flag = True
#     number = randint(0, 20)
#     if number not in list_2:
#         list_2.append(number)
#     else:
#         while flag:
#             number = randint(0, 20)
#             if number not in list_2:
#                 list_2.append(number)
#                 flag = False
# print(list_2)

# # лень делать еще цикл, поэтому поконвертила
# result_set = set(list_1).intersection(set(list_2))
# result_list = list(result_set)

# # быстрая сортировка
# def quicksort(list_for_sort):
#     if len(list_for_sort) < 2:
#         return list_for_sort
#     else:
#         middle = list_for_sort[0]
#         small = [i for i in list_for_sort[1:] if i < middle]
#         big = [i for i in list_for_sort[1:] if i > middle]
#         return quicksort(small) + [middle] + quicksort(big)
# print(quicksort(result_list))

# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.

# n = int(input("Введите количество кустов: "))
# berries = []
# berries_max = 0
# bush_index = 0

# while len(berries) < n:
#     berries.append(randint(0, 20))

# print(berries)

# for i in range(len(berries)):
#     if i+1 >= len(berries):
#         if (berries[i-1] + berries[i] + berries[0]) > berries_max:
#             berries_max = berries[i-1] + berries[i] + berries[i+1]
#             bush_index = i
#     elif (berries[i-1] + berries[i] + berries[i+1]) > berries_max:
#         berries_max = berries[i-1] + berries[i] + berries[i+1]
#         bush_index = i
# print(
#     f"Максимальное количество ягод - {berries_max}, лучший средний куст - {bush_index}")
