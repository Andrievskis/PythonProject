def get_mask_card_number(number_card: str) -> str:
    """Функция, возвращающая маскировку номера карты."""
    if len(number_card) == 0:
        raise ValueError("Вы не ввели номер карты!")
    number_card_list = list(number_card)
    number_card_list[6:-4] = "*" * len(number_card_list[6:-4])
    number_card_str = "".join(number_card_list)
    return " ".join([number_card_str[i:i + 4] for i in range(0, len(number_card_str), 4)])


# Маскировка номера карты.
# print(get_mask_card_number("7000792289606361000"))


def get_mask_account(number_account: str) -> str:
    """Функция, возвращающая маскировку номера счета."""
    mask_account = number_account.replace(number_account[:-4], "**")
    if len(number_account) != 20 and number_account.isdigit():
        raise ValueError("Введите корректный номера счета состоящий из 20 цифр!")
    if len(number_account) == 0:
        raise ValueError("Вы не ввели номер счета!")
    return mask_account


# Маскировка номера счета.
# print(get_mask_account("70007922896063610000"))
