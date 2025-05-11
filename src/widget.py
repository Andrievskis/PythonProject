from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция, обрабатывающая информацию о картах и счетах."""
    if number == "":
        raise ValueError("Вы не ввели номер счета (карты)!")
    if str(number).isdigit() or str(number).isalpha():
        raise ValueError("Введите корректный номер! Вы ввели только буквы (или только цифры)!")
    number_name_list = number.split()
    if (
        len(number_name_list[-1]) == 16
        or len(number_name_list[-1]) == 13
        or len(number_name_list[-1]) == 19
        or len(number_name_list[-1]) == 15
    ):
        number_name_list[-1] = get_mask_card_number(number_name_list[-1])
    elif len(number_name_list[-1]) == 20:
        number_name_list[-1] = get_mask_account(number_name_list[-1])
    number_name_list_str = " ".join(number_name_list)
    return number_name_list_str


# Обработка названия и маскировка карт/счета.
# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(mask_account_card("Maestro 7000792289606361"))
# print(mask_account_card("Счет 73654108430135874305"))

# Обработка передачи пустой информации. ValueError: Вы не ввели номер счета (карты)!
# print(mask_account_card(""))

# Некорректный ввод информации (введены только цифры).
# ValueError: Введите корректный номер! Вы ввели только буквы (или только цифры)!
# print(mask_account_card("7000792289606361"))
# print(mask_account_card(987654321245678))

# Некорректный ввод информации (введены только буквы).
# ValueError: Введите корректный номер! Вы ввели только буквы (или только цифры)!
# print(mask_account_card("Счет"))
# print(mask_account_card("Maestro"))
# print(mask_account_card(None))


def get_date(date_: str) -> str:
    """Функция, для изменения формата даты."""
    try:
        dt = datetime.strptime(date_, "%Y-%m-%dT%H:%M:%S.%f")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат ввода даты. Введите корректный формат даты!")


# Обработка некорректоного формата ввода для данной функции.
# ValueError: Некорректный формат ввода даты. Введите корректный формат даты!
# print(get_date("2024-03-11"))

# Обработка корректоного формата ввода для данной функции. 11.03.2024
# print(get_date("2024-03-11T02:26:18.671407"))
