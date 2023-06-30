# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
from random import randint


# def fibonachi(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonachi(n-1) + fibonachi(n-2)


# print(fibonachi(5))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# list = [1, 2, 5, 4, 6, 5, 2, 1, 10, 6, 8, 10]
# list_1 = []

# num = int(input('Введите количество оценок: '))
# for i in range(num):
#     list_1.append(randint(1, 10))
# print(f'Текущий: {list_1}', end="\n")

# max1 = max(list_1)
# min1 = min(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max1:
#         list_1[i] = min1

# print(list_1)

# print(list_2 := [i for i in list_1])
# print([i if i != max1 else min1 for i in list_2])

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# def Prostoe(n):
#     for i in range(2,n):
#         if n%i==0:
#             return "Непростое"
#     return "Простое"

# print(Prostoe(7))

# Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.
# n = int(input("Введите натуральное число: "))


# def Sequence(n):
#     if n == 0:
#         return n
#     print(n, end=' ')
#     return Sequence(n-1)


# Sequence(n)

# Последовательностью Фибоначчи называется последовательность чисел
# def fibo(v):
#     if v == 0:
#         return 0
#     if v == 1:
#         return 1
#     return fibo(v-1) + fibo(v-2)
# print(fibo(7))

#
# list_lang = int(input("Введите длину: "))
# list_1 = []


# def create_list():
#     for i in range(list_lang):
#         list_1.append(randint(1, 10))
#     return list_1


# print(f"Изначально: {create_list()}")

# min_mark = min(list_1)
# max_mark = max(list_1)


# def change(list_1):
#     for i in range(len(list_1)):
#         if list_1[i] == max_mark:
#             list_1[i] = min_mark
#     return list_1


# print(f"Неначально: {change(list_1)}")

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# n = int(input("Введите число: "))

# def prostoe(n):
#     if n in [1, 2]:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, n):
#         if n % i == 0:
#             return False
#     return True

# print(prostoe(n))

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# def create_list(n):
#     num = input('')
#     if n == 1:
#         return num
#     return create_list(n-1) + ' ' + num

# # f(2) + 3
# # f(1) + 4 + 3
# # 5 + 4 + 3 --> 543
# n = int(input('--> '))
# res = create_list(n)
# print(res)
