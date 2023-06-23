from random import randint
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# k = int(input("Введите число: "))
list_1 = 1, 2, 3, 4, 5, 6, 7
# list_2 = []
# for i in range(len(list_1)-k):
#     a = list_1.pop(0)
#     list_2.append(a)
# for j in range(len(list_1)):
#     list_2.insert(j, list_1[j])
# print(list_2)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# print(list_1 := [randint(1, 10) for i in range(10)])

# count = 0
# for i in range(len(list_1)-1):
#     if (list_1[i] < list_1[i+1]):
#         count += 1
# print(count)

# Напишите программу для печати всех уникальных значений в словаре.

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
#     "VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {"VIII": "S007"}]
# list_2 = set()
# for i in list_1:
#     for k in i.values():
#         list_2.add(k)
# print(list_2)

# print(set(k for i in range(len(list_1)-1) for (j, k) in list_1[i].items()))

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# arr = [1, 1, 2, 5, 2, 3, 2, 3, 5, 5, 8]
# arrat_2 = set(arr)
# print(arrat_2)
# print(len(arrat_2))

# array_3 = {1, 1, 2, 5, 2, 3, 2, 3, 5, 5, 8, "asd"}
# print(len(array_3))

# for i in array_3:
#     print(i)

# count = len(arr)
# total = 0
# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j]:
#             total += 1
#             count -= 1
# print(total)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 89]

# k = int(input("Введите число: "))
# result = list_1[6:8] + list_1[0:6]
# result = list_1[len(list_1)-k:] + list_1[:len(list_1)-k]
# print(result)

# a = [1, 2, 3, 4, 5]
# k = int(input("asd"))
# for i in range(k):
#     a.insert(0, a.pop())
# print(a)

# Напишите программу для печати всех уникальных значений в словаре.

# Input = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
#     "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# result = set()
# for i in Input:
#     for k in i.values():
#         result.add(k)

# print(set(result for i in Input for result in i.values()))

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# list_1 = [1, 1, 2, 52, 1, 4, 5, 63, 2, 1]
# count = 0
# for i in range(len(list_1)-1):
#     if list_1[i+1] > list_1[i]:
#         count += 1
# print(count)
