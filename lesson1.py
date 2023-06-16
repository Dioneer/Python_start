import math
# python -m venv .folder
# print(5)
# print(5)
# print(5)
# print(5)
# a = int(input("Enter item: "))
# b = int(input("Enter item: "))
# print(f"{a} + {b} = {a+b}")

# c = 1.251
# d = 1.235
# print(round(c*d, 1))

# for i in range(100, 0, -20):
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# def countsort(A, max):

# создает список целых чисел размером `k + 1` для хранения количества каждого целого числа.
# в списке ввода
#  freq = [0 for i in range(max)]

# , используя значение каждого элемента в списке ввода в качестве индекса,
# сохраняет счетчик каждого целого числа в `freq[]`
#  for i in A:
#      freq[i] += 1

# перезаписывает входной список в отсортированном порядке
#     index = 0
#     for i in range(max):
#         while freq[i] > 0:
#             A[index] = i
#             index += 1
#             freq[i] -= 1


# if __name__ == '__main__':

#     A = [4, 2, 10, 10, 1, 4, 2, 1, 10]

# диапазон элементов списка
#     max = 11

#     countsort(A, max)
#     print(A)


# print(5+True)

# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами. Input: n = 700 m = 750 Output: 2


# m = int(input("Введите количество километров, которые проехала машина во второй раз: "))
# n = int(input("Введите количество километров, которые проехала машина в первый раз за один день: "))

# print(f"Количество дней: {m / n}")

# kabinet1 = int(input("Введи количество учащихся:"))
# kabinet2 = int(input("Введи количество учащихся:"))
# kabinet3 = int(input("Введи количество учащихся:"))
# o = math.ceil(kabinet1/2) + math.ceil(kabinet2/2)+math.ceil(kabinet3/2)

# print(f"итого парт: {o}")

# print(7//2)


# m = (int(input('Введите количество клометров, которые проехали за 1 день: ')))
# n = (int(input('Введите количество клометров, которые проехали всего: ')))
# print(f'Требуется {(n//m)+ (n%m>0)} дней')

# class1 = int(input('Введите количество детей в классе 1: '))
# class2 = int(input('Введите количество детей в классе 2: '))
# class3 = int(input('Введите количество детей в классе 3: '))
# print(
#     f'Всего парт - {class1 //2 + class1%2 + class2 //2 + class2%2 + class3 //2+class3%2}')

# year = int(input('Введите год: '))
# if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
#     print(f"{year} високосный")
# else:
#     print(f"{year} не високосный")
