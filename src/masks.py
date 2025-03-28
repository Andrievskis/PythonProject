def get_mask_card_number(number_card: str) -> str:
    """Функция, возвращающая маскировку номера карты."""
    number_card_list = list(number_card)
    number_card_list[6:-4] = "*" * len(number_card_list[6:-4])
    number_card_str = "".join(number_card_list)
    return " ".join([number_card_str[i:i + 4] for i in range(0, len(number_card_str), 4)])


# print(get_mask_card_number("7000792289606361"))


def get_mask_account(number_account: str) -> str:
    """Функция, возвращающая маскировку номера счета."""
    mask_account = number_account.replace(number_account[:-4], "**")
    return mask_account


# print(get_mask_account("73654108430135874305"))
