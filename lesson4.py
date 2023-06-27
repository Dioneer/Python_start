# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных слов содержится в этом тексте.
# text = "Словом - считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных слов содержится в этом тексте."

# list_dict = ''.join([chr(i) for i in range(ord('а'), ord('я')+1)]) + 'ё'
# words = []
# word = ''

# for ch in text.lower():
#     if ch in list_dict:
#         word += ch
#     else:
#         if word != '':
#             words.append(word)
#             word = ''
# print(words)

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# text = '1234567895466666'
# temp = {}

# for i in range(len(text)):
#     temp[text[i]] = 0

# for i in range(len(text)):
#     if text[i] in temp.keys():
#         temp[text[i]] += 1

# for i, k in temp.items():
#     print(f"{i}_{k}", end=(" "))

# for i in range(len(text)):
#     if [i] not in temp.keys():
#         temp[text[i]] = 1
#         result += f'{text[i]}_{temp[text[i]]} '
#     else:
#         result += f'{text[i]}_{temp[text[i]]} '
#         temp[text[i]] += 1
# print(result)

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# input = 'a a a b c a a d c d d'
# list = input.split()
# list_2 = {}

# for i in range(len(list)):
#     if list[i] not in list_2.keys():
#         list_2[list[i]] = 0
#         print(f'{list[i]} ', end='')
#     else:
#         list_2[list[i]] += 1
#         print(f'{list[i]}_{list_2[list[i]]} ', end='')

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним пробелом. Определите, сколько различных слов содержится в этом тексте.

# text_string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(text_string.split())
# print(len(set(text_string.lower().split())))
# print(text_string.isdigit())
# print(ord('a'), ord('z'))


# income = int(input("Введите число: "))
# maximum = income
# while income > 0:
#     income = int(input("Введите число: "))
#     if maximum < income:
#         maximum = income
# print(maximum)
