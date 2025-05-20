def get_mask_card_number(number_card: str) -> str:
    """Функция, возвращающая маскировку номера карты."""
    if not isinstance(number_card, str):
        raise TypeError("Ошибка типа данных.")
    elif len(number_card) == 0:
        raise ValueError("Вы не ввели номер карты!")
    elif (
        (number_card[-1].isdigit() and len(number_card) == 16)
        or (number_card[-1].isdigit() and len(number_card) == 15)
        or (number_card[-1].isdigit() and len(number_card) == 19)
        or (number_card[-1].isdigit() and len(number_card) == 13)
    ):
        number_card_list = list(number_card)
        number_card_list[6:-4] = "*" * len(number_card_list[6:-4])
        number_card_str = "".join(number_card_list)
        return " ".join([number_card_str[i:i + 4] for i in range(0, len(number_card_str), 4)])
    else:
        raise ValueError("Вы ввели некорректный номер карты!")


# Маскировка номера карты.
print(get_mask_card_number("7000792289606361000"))

# ValueError: Вы ввели некорректный номер карты! (длинна номера карты должна быть 13, 15, 16 или 19 и только цифры)
# print(get_mask_card_number("700079"))
# print(get_mask_card_number('aaaaaaaaaaaaa'))

# TypeError: Ошибка типа данных.
# print(get_mask_card_number(7000792289606361000))

# ValueError: Вы не ввели номер карты!
# print(get_mask_card_number(""))


def get_mask_account(number_account: str) -> str:
    """Функция, возвращающая маскировку номера счета."""
    if not isinstance(number_account, str):
        raise TypeError("Ошибка типа данных.")
    elif len(number_account) == 0:
        raise ValueError("Вы не ввели номер счета!")
    elif len(number_account) == 20 and number_account.isdigit():
        mask_account = number_account.replace(number_account[:-4], "**")
        return mask_account
    else:
        raise ValueError("Вы ввели некорректный номер счета!")


# Маскировка номера счета.
# print(get_mask_account("70007922896063610009"))


# TypeError: Ошибка типа данных.
# print(get_mask_account(70007922896063610000))


# ValueError: Вы не ввели номер счета!
# print(get_mask_account(""))


# ValueError: Вы ввели некорректный номер счета!
# print(get_mask_account("7000"))
