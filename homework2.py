from random import randint
# На столе лежит n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# def coins():
#     quantity = int(input("Введите количество монеток: "))
#     heads = 0
#     tails = 0
#     for i in range(quantity):
#         coin = randint(0, 1)
#         print(coin)
#         if (coin == 0):
#             heads += 1
#         else:
#             tails += 1
#     print(f'Надо перевернуть {tails} монет' if tails <=
#           heads else f'Надо перевернуть {heads} монет')
# coins()

# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.


# def riddles():
#     num1 = int(input("Введите первое число:"))
#     num2 = int(input("Введите второе число:"))
#     for i in range(1000):
#         for j in range(1000):
#             if ((i+j == num1) and (i*j == num2)):
#                 return print(f"His numbers is {i} and {j}")
#     return print(f"The riddle has no answers")


# riddles()

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# def degree():
#     n_number = int(input("Введите число: "))
#     dyad = 0
#     two = 2
#     array = []
#     while two**dyad <= n_number:
#         array.append(two**dyad)
#         dyad += 1
#     print(array)

# degree()
