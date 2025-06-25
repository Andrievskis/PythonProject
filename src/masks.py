import logging

logger = logging.getLogger("masks_log")
file_handler = logging.FileHandler(
    "/Users/anastasiaandreeva/PycharmProjects/PythonProject/logs/masks.log", "w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: str) -> str:
    """Функция, возвращающая маскировку номера карты."""
    logger.warning("Тип ввода данных - str!")
    if not isinstance(number_card, str):
        logger.error(f"Ошибка типа данных {type(number_card)}.")
        raise TypeError("Ошибка типа данных.")
    elif len(number_card) == 0:
        logger.error(f"Вы не ввели номер карты: {number_card}")
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
        number_card_ = " ".join([number_card_str[i:i + 4] for i in range(0, len(number_card_str), 4)])
        logger.info(f"Ваш маскированный номер карты: {number_card_}.")
        return number_card_
    else:
        logger.error(f"Вы ввели некорректный номер карты: {number_card}")
        raise ValueError("Вы ввели некорректный номер карты!")


# Маскировка номера карты.
# print(get_mask_card_number("7000792289606361000"))


def get_mask_account(number_account: str) -> str:
    """Функция, возвращающая маскировку номера счета."""
    logger.warning("Тип ввода данных - str!")
    if not isinstance(number_account, str):
        logger.error(f"Ошибка типа данных {type(number_account)}.")
        raise TypeError("Ошибка типа данных.")
    elif len(number_account) == 0:
        logger.error(f"Вы не ввели номер карты: {number_account}")
        raise ValueError("Вы не ввели номер счета!")
    elif len(number_account) == 20 and number_account.isdigit():
        mask_account = number_account.replace(number_account[:-4], "**")
        logger.info(f"Ваш маскированный номер счета: {mask_account}.")
        return mask_account
    else:
        logger.error(f"Вы ввели некорректный номер счета: {number_account}")
        raise ValueError("Вы ввели некорректный номер счета!")


# Маскировка номера счета.
# print(get_mask_account("70007922896063610009"))
