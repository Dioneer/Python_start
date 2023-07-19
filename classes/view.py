import text
from module import PhoneBook


def print_msg(msg: str):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg)+'\n')


def show_menu(menu: list[str]) -> int:
    for i, item in enumerate(menu):
        if i != 0:
            print(f"\t{i}. {item}")
        else:
            print(item)
    input_select = input("Выберите пункт меню: ")
    while True:
        if input_select.isdigit() and 0 < int(input_select) < len(menu):
            return int(input_select)
        input_select = input(text.menu_error)


def show_contacts(book: PhoneBook, msg: str):
    if book:
        max_n, max_p, max_c = book.max_len()
        print('\n'+'='*(sum(book.max_len())+17))
        print(
            f'{"ID": >3}. {"Фамилия и имя": <{max_n}}  'f'{"Телефон": <{max_p}}  'f'{"Комментарий": <{max_c}}')
        print()
        for i, item in book.phone_book.items():
            print(f'{i: >3}. {item.show(max_n, max_p, max_c)}')
        print('='*(sum(book.max_len())+17)+'\n')
    else:
        print_msg(msg)


def contact_input(input_fields: list[str]) -> list[str]:
    contact = []
    for item in input_fields:
        contact.append(input(item))
    return contact


def input_data(msg: str) -> str:
    return input(msg)


def input_number(msg: str) -> int:
    while True:
        number = input(msg)
        if number.isdigit():
            return int(number)
        print(text.number_error)
