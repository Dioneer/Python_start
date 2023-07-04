# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
from random import randint

# list1 = [randint(1, 50) for i in range(randint(5, 20))]
# list2 = [randint(1, 50) for i in range(randint(5, 20))]
# print(list1)
# print(list2)


# def not_intersection(l1, l2):
#     l3 = []
#     for i in range(len(l1)-1):
#         if l1[i] not in l2:
#             l3.append(l1[i])
#     return l3


# list3 = not_intersection(list1, list2)
# print(list3)

# print(first := [randint(1, 50) for i in range(randint(5, 20))])
# print(second := [randint(1, 50) for i in range(randint(5, 20))])

# print([item for item in first if item not in second])

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.

# print(list_1 := [randint(1, 10) for i in range(10)])
# count = 0
# for i in range(1, len(list_1)-1):
#     if list_1[i-1] < list_1[i] > list_1[i+1]:
#         count += 1
# print(count)

# print(len([i for i in range(1, len(list_1)-1)
#       if list_1[i-1] < list_1[i] > list_1[i+1]]))

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

# print(list_1 := [randint(1, 10) for i in range(10)])
# count = 0
# for i in range(len(list_1)-1):
#     if list_1[i] == list_1[i+1]:
#         count += 1
#         i += 2
#     else:
#         i += 1
# print(count)

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.

# def summ_del(num):
#     sum1 = 0
#     for i in range(1, num//2 + 1):
#         if num % i == 0:
#             sum1 += i
#     return sum1


# third = []
# for i in range(1, 10000):
#     second = summ_del(i)
#     first = summ_del(second)
#     if i == first and i < second:
#         print(i, second)

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве выведет количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.

# print(list := [randint(1, 10) for i in range(randint(8, 10))])
# print(len([i for i in range(1, len(list)-1) if list[i-1] < list[i] > list[i+1]]))

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.

# print(list := [randint(1, 10) for i in range(randint(8, 10))])
# list2 = []
# for i in range(len(list)-1):
#     for j in range(i+1, len(list)):
#         if list[i] == list[j]:
#             list2.append(list[j])
# print(len(list2))

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.

# def division(num):
#     sum = 0
#     for i in range(1, num//2+1):
#         if num % i == 0:
#             sum += i
#     return sum


# def check(k):
#     for i in range(1, k):
#         start = division(i)
#         end = division(start)
#         if i == end and i != start and i < start:
#             print(i, start)


# k = int(input('Enter number: '))

# check(k)
