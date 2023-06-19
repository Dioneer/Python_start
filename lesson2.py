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
