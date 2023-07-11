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


def change_to_string(item):
    result = ''
    for i in range(len(item)):
        for k in item[i].values():
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
    file.writelines(change_to_string(dict_for_all))
    dict_for_all.clear()
    file.close()


def remove_contact(n):
    file = open(r'append.txt', 'w', encoding='utf8')
    file.writelines(change_to_string(n))
    file.close()


def add_contact():
    dict_for_all.clear()
    name, phone, comm = input("Введите данные: ").strip().split(';')
    dict_for_all.append({'name': name, 'phone': phone, 'comm': comm})
    close_contact()


def show_contact():
    dict_for_all.clear()
    open_contact()
    print([i for i in dict_for_all], sep='\n')


def find_contact():
    dict_for_all.clear()
    search = input('Введите искомое: ').strip()
    result = []
    open_contact()
    for i in dict_for_all:
        if search in i['name'] or search in i['phone'] or search in i['comm']:
            result.append(i)
    print(*[i for i in result])
    return result


def change_contact():
    dict_for_all.clear()
    open_contact()
    not_use = []
    useable = []
    keych, value = input(
        'Что требуется изменить, введите ключ и на что менять через пробел: ').strip().split()
    for i in dict_for_all:
        if (keych not in i['name']) and (keych not in i['phone']) and (keych not in i['comm']):
            not_use.append(i)
        if (keych in i['name']) or (keych in i['phone']) or (keych in i['comm']):
            useable.append(i)
    for i in useable:
        for j, k in i.items():
            if keych in k:
                i[j] = k.replace(keych, value)
    for i in useable:
        not_use.append(i)
    remove_contact(not_use)


def del_contact():
    dict_for_all.clear()
    list_1 = []
    search = input('Введите искомое: ').strip()
    open_contact()
    for i in dict_for_all:
        if (search not in i['name']) and (search not in i['phone']) and (search not in i['comm']):
            list_1.append(i)
    remove_contact(list_1)


def choice_user():
    flag = True
    while flag:
        start = input("1.Открыть файл\n 2. Сохранить файл\n 3. Показать контакты\n 4. Добавить контакт\n 5. Найти контакт\n 6. Изменить контакт\n 7. Удалить контакт\n 8. Выход\n выберите пункт меню: ")
        match start:
            case '1':
                print("лучше не держать поток открытым все время")
            case '2':
                close_contact()
                print("просто закрывается, если открыт но этого не видно")
            case '3':
                show_contact()
            case '4':
                add_contact()
            case '5':
                find_contact()
            case '6':
                change_contact()
            case '7':
                del_contact()
            case '8':
                flag = False
            case _:
                print('такой команды нет.')
                flag = False


choice_user()
