from pathlib import Path
from copy import deepcopy


class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_str(self):
        return f"{self.name} {self.phone} {self.comment}".lower()

    def to_list(self):
        return [self.name, self.phone, self.comment]

    def show(self, max_n: int, max_p: int, max_c: int) -> str:
        return f"{self.name: <{max_n}} {self.phone: <{max_p}} {self.comment: <{max_c}}"


class PhoneBook:
    def __init__(self, phone_book: dict[int, Contact] = None, path: str = 'append_file.txt'):
        if phone_book is None:
            self.phone_book = {}
            self.id = 1
        else:
            self.phone_book = phone_book
            self.id = max(phone_book)+1
        self.file_path = Path('classes', path)
        self. original_pb = {}
        self.id = 1

    def open_file(self):
        with open(self.file_path, 'r', encoding='utf8') as file:
            contacts = file.readlines()
        for contact in contacts:
            uid, name, phone, comment = contact.strip().split(';')
            self.phone_book[int(uid)] = Contact(name, phone, comment)
        self.id = max(self.phone_book)+1
        self.original_pb = deepcopy(self.phone_book)

    def add_contact(self, new: list[str]):
        self.phone_book[self.id] = Contact(*new)
        self.id + 1

    def save_file(self):
        with open(self.file_path, 'w', encoding='utf8') as file:
            contacts = []
            for uid, contactio in self.phone_book.items():
                contacts.append(
                    ';'.join([str(uid), *contactio]))
            contacts = '\n'.join(contacts)
            file.write(contacts)
        self.original_pb = deepcopy(self.phone_book)

    def search_request(self, word: str) -> dict[int, Contact]:
        result = {}
        for i, contact in self.phone_book.items():
            if word.lower() in contact.to_str():
                result[i] = contact
        return result

    def change_contact(self, uid: int, new: list[str]) -> str:
        contact = self.phone_book.get(uid).to_list()
        for i in range(len(contact)):
            if new[i] != '':
                contact[i] = new[i]
        self.phone_book[uid] = Contact(*contact)
        return contact[0]

    def delete_contact(self, uid: int) -> str:
        return self.phone_book.pop(uid).name

    def max_len(self):
        result = [[], [], []]
        for contact in self.phone_book.values():
            for i, item in enumerate(contact.to_list()):
                result[i].append(item)
        return list(map(lambda x: len(max(x, key=len)), result))
