# from calendar import isleap

# Проверка на високосность=================================

# вариант 1
# year = int(input('Введите год: '))
# if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
#     print(f"{year} високосный")
# else:
#     print(f"{year} не високосный")

# вариант 2
# year = int(input('Введите год: '))
# if (year % 4 == 0) and (year % 100 != 0):
#     print(f"{year} високосный")
# elif year % 400 == 0:
#     print(f"{year} високосный")
# else:
#     print(f"{year} не високосный")

# вариант 3
# year = int(input('Введите год: '))
# if isleap(year):
#     print(f"{year} високосный")
# else:
#     print(f"{year} не високосный")

# Найдите сумму цифр трехзначного числа=======================================

# вариант 1
# number = int(input("Введите число: "))
# summ = 0
# while number > 0:
#     summ += number % 10
#     number = number//10
# print(f"the sum of the digits is: {summ}")

# вариант 2
# number = input("Введите число: ")
# print(sum(map(int, number)))

# Петя, Катя и Сережа делают из бумаги журавликов================================

# вариант 1
# crane = int(input("Введите количество журавликов: "))
# if crane % 2 != 0:
#     print(f"Такое, в принципе, возможно, но это значит, что журавлики недоделаны")
# else:
#     parts = crane/6
#     petr = parts
#     kate = (petr + petr)*2
#     print(f"Катя сделала {kate}, Петя {petr}, Сергей {petr}")

# вариант 2
# crane = int(input("Введите количество журавликов: "))
# print(f"{crane / 6} {crane/ 6 * 4} {crane/ 6}")

# Вам требуется написать программу, которая проверяет счастливость билета============

# вариант 1
# tiket = input("Введите номер билета:")
# part1 = int(tiket[0]) + int(tiket[1]) + int(tiket[2])
# part2 = int(tiket[3]) + int(tiket[4]) + int(tiket[5])
# if part1 == part2:
#     print('Билет частливый')
# else:
#     print('Билет бычный')

# вариант 2
# tiket = input("Введите номер билета:")
# part1 = sum(map(int, tiket[:3]))
# part2 = sum(map(int, tiket[3:]))
# if part1 == part2:
#     print('Билет частливый')
# else:
#     print('Билет бычный')

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек

# вариант 1
