from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция, обрабатывающая информацию о картах и счетах."""
    number_name_list = number.split()
    number_name_list[-1] = get_mask_card_number(number_name_list[-1])
    if number_name_list[0] == "Счет":
        number_name_list[-1] = get_mask_account(number_name_list[-1])
    number_name_list_str = " ".join(number_name_list)
    return number_name_list_str


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_: str) -> str:
    """Функция, для изменения формата даты."""
    dt = datetime.strptime(date_, "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
