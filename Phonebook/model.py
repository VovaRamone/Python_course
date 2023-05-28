phone_book: list[dict[str, str]] = []
path = 'phonebook.txt'


def open_pb():
    global phone_book
    phone_book.clear()  # Clear the phone_book list before populating it
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]}
        phone_book.append(new)


def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        contact_info = [
            contact.get('id'),
            contact.get('name'),
            contact.get('phone'),
            contact.get('comment')
        ]
        data.append(':'.join(contact_info))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_pb():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> str:
    global phone_book
    new_id = str(len(phone_book) + 1)  # Generate a new ID based on the length of the phone book
    new['id'] = new_id
    phone_book.append(new)
    return new.get('name')


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result: list[dict[str, str]] = []
    for contact in phone_book:
        for field in contact.values():
            if word.lower() in field.lower():
                result.append(contact)
                break
    return result


def change_contact(new: dict, index: int) -> str:
    global phone_book
    for contact in phone_book:
        if index == contact.get('id'):
            contact['name'] = new.get('name', contact.get('name'))
            contact['phone'] = new.get('phone', contact.get('phone'))
            contact['comment'] = new.get('comment', contact.get('comment'))
            return contact.get('name')


# def delete_contact(contact_id: str) -> str:
#     global phone_book
#     for contact in phone_book:
#         if contact["id"] == contact_id:
#             name = contact["name"]
#             phone_book.remove(contact)
#             return name
#     return ""






def delete_contact(contact_id: str) -> str:
    global phone_book
    for contact in phone_book:
        if contact["id"] == contact_id:
            name = contact["name"]
            phone_book.remove(contact)
            return name
    return ""