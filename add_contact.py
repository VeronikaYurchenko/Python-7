# Запись конакта в телефонную книгу

def add_contact():
    contact = []
    name = input('Введите имя: ')
    contact.append(name.title())
    surname = input('Введите фамилию: ')
    contact.append(surname.title())
    phone_number = input('Введите номер телефона: ')
    contact.append(phone_number)
    any_info = input('Комментарии: ')
    contact.append(any_info.title())
    print('Абонент записан: ', contact)
    return contact