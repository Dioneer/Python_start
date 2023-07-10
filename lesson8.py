# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход


# Панфилов Кирилл;89094512021;Семнарист GB
# Роберт Адамян;888-999-777;DJ на семинарах

dict_for_all = []


def change_to_string(dict_for_all):
    result = ''
    for i in range(len(dict_for_all)):
        for k in dict_for_all[i].values():
            result += f'{k};'
        result += '\n'
    return result


def change_to_object(file):
    liststring = file.split(';')
    listKeys = ['name', 'phone', 'comm']
    dict_for_all.append({listKeys[i]: liststring[i]
                        for i in range(len(liststring)-1)})
    return dict_for_all


def open_contact():
    file = open(r'append.txt', 'r', encoding='utf8')
    for line in file:
        change_to_object(line)
    file.close()


def close_contact():
    file = open(r'append.txt', 'a', encoding='utf8')
    print(change_to_string(dict_for_all))
    file.writelines(change_to_string(dict_for_all))
    dict_for_all.clear()
    file.close()


def add_contact():
    name, phone, comm = input("Введите данные: ").split(';')
    dict_for_all.append({'name': name, 'phone': phone, 'comm': comm})
    key = input("Если требутся продложение, то введите '1' иначе '2': ")
    return choice_user(key)


def show_contact():
    open_contact()
    print(*[i for i in dict_for_all], sep='\n')


def find_contact():
    search = input('Введите искомое: ').strip()
    print(search)
    result = []
    open_contact()
    for i in dict_for_all:
        if i['name'] == search or i['phone'] == search or i['comm'] == search:
            result.append(i)
    print(*[i for i in result], sep='\n')
    return result


def change_contact():
    find = find_contact()
    keych, value = input(
        'Что требуется изменить, введите ключ и на что менять: ').strip().split()
    for i in find:
        i[keych] = value
    print(*[i for i in find], sep='\n')
    return find


def del_contact():
    search = input('Введите искомое: ').strip()
    open_contact()
    for i in dict_for_all:
        if i['name'] == search or i['phone'] == search or i['comm'] == search:
            dict_for_all.pop(dict_for_all.index(i))
    close_contact()
    return dict_for_all


def exit_contact():
    return


def choice_user(key_menu):
    flag = True
    while flag:
        match key_menu:
            case '1':
                print("лучше не держать поток открытым все время")
                flag = False
                return
            case '2':
                close_contact()
                print("просто закрывается, если открыт но этого не видно")
                flag = False
            case '3':
                show_contact()
                flag = False
            case '4':
                add_contact()
                flag = False
            case '5':
                find_contact()
                flag = False
            case '6':
                change_contact()
                flag = False
            case '7':
                del_contact()
                flag = False
            case '8':
                exit_contact()
                flag = False
            case _:
                print('такой команды нет.')
                flag = False


start = input('Press any key or space for finish: ')
if start:
    key_menu = input("1.Открыть файл\n 2. Сохранить файл\n 3. Показать контакты\n 4. Добавить контакт\n 5. Найти контакт\n 6. Изменить контакт\n 7. Удалить контакт\n 8. Выход\n выберите пункт меню: ")
    choice_user(key_menu)
else:
    print('BY')
