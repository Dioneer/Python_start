# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# n = int(input('Введите число:'))
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print(fact)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# fibonachiLi = int(input("Введите число: "))
# result = -1
# fib_sum = 0
# temp = 0
# temp2 = 1
# index = 0
# print(index)
# while fib_sum <= fibonachiLi:
#     fib_sum = temp + temp2
#     temp = temp2
#     temp2 = fib_sum
#     index += 1

# if (temp == fibonachiLi):
#     print(index)
# else:
#     print(result)

# По данному целому неотрицательному n вычислите значение n!.
# fact = int(input("Введите число: "))
# result = 1
# while fact > 0:
#     result *= fact
#     fact -= 1
# print(result)

# n = int(input('Enter number pls: '))
# i = 1
# fact = 1
# while i <= n:
#     fact, i = fact*i, i+1
# print(fact)

# fibo = int(input("Введите число: "))
# tepm1 = 0
# tepm2 = 1
# index = 2
# while tepm2 < fibo:
#     tepm1, tepm2, index = tepm2, tepm1+tepm2, index + 1
# if tepm2 == fibo:
#     print(index)
# else:
#     print(-1)

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# n = int(input("Введите число дней: "))
# counter = 0
# maxValue = 0
# for number in range(n):
#     newNumber = int(input("Введите число: "))
#     if newNumber > 0:
#         counter += 1
#     elif counter > maxValue:
#         maxValue = counter
#     elif newNumber < 0:
#         counter = 0
# print(maxValue)

# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# n = int(input("Введите количество арбузов: "))
# x = int(input("Введите массу арбуза - "))
# minWeigt = x
# maxWeight = x
# for i in range(n-1):
#     x = int(input("Введите массу арбуза - "))
#     if x<minWeigt:
#         minWeigt = x
#     if x>maxWeight:
#         maxWeight = x

# print(minWeigt, maxWeight)
