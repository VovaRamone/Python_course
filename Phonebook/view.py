import text
import colorama
from tabulate import tabulate

colorama.init()

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    if book:
        headers = [
            colorama.Fore.BLUE + "ID" + colorama.Style.RESET_ALL,
            colorama.Fore.GREEN + "Name" + colorama.Style.RESET_ALL,
            colorama.Fore.YELLOW + "Phone" + colorama.Style.RESET_ALL,
            colorama.Fore.MAGENTA + "Comment" + colorama.Style.RESET_ALL
        ]
        table_data = []
        for contact in book:
            row = [
                colorama.Fore.BLUE + contact.get("id") + colorama.Style.RESET_ALL,
                colorama.Fore.GREEN + contact.get("name") + colorama.Style.RESET_ALL,
                colorama.Fore.YELLOW + contact.get("phone") + colorama.Style.RESET_ALL,
                colorama.Fore.MAGENTA + contact.get("comment") + colorama.Style.RESET_ALL
            ]
            table_data.append(row)
        table = tabulate(table_data, headers, tablefmt="double_grid")
        print(table)
    else:
        print_message(error)

def input_contact(message) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_contact.items():
        value = input(txt)
        if value:
            new[key] = value
    return new


def input_search(message) -> str:
    return input(message)


def input_index(message) -> int:
    return int(input(message))


def ask_save_before_exit() -> bool:
    choice = input(text.ask_save_before_exit)
    return choice.lower() == 'y'

