#  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# a = int(input("Введите число: "))
# b = int(input("Введите степень: "))

# def pow(a, b):
#     if b == 0:
#         return 1
#     if b < 0:
#         return 1/pow(a, -b)
#     return a * pow(a, b-1)
# print(pow(a, b))


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# def summa(a, b):
#     if a == 0:
#         return b
#     return summa(a-1, b+1)


# print(summa(3, 5))