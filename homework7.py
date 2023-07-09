#  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.

# def counter(words):
#     if (list_1 == 'number'):
#         return print('Число или пробел')
#     result = set(map(lambda x: sum(
#         1 for i in words[words.index(x)] if i in 'аеёиоуыэюя'), list_1))
#     if len(result) < 2:
#         return print('Парам пам-пам')
#     return print('Пам парам')


# list_1 = input('Введите текст: ')
# list_1 = 'number' if list_1.isdigit(
# ) or list_1 == '' else list_1.lower().split()
# counter(list_1)

#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print(*[[operation(i, j) for j in range(1, num_columns + 1)]
#             for i in range(1, num_rows + 1)], sep=",\n")


# num, num_1 = list(map(int, (input('Введите ширину и высоту: ').split())))
# print_operation_table(lambda x, y: x * y, num, num_1)
