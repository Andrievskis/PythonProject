from typing import Any, Iterator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 167764268,
        "state": "EXECUTED",
        "date": "2020-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "from": "Счет 19708645243227258542",
        "description": "Перевод со счета на счет",
        "to": "Счет 756516673830602841455",
    },
]

transactions_for_func_descriptions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 167764268,
        "state": "EXECUTED",
        "date": "2020-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "from": "Счет 19708645243227258542",
        "to": "Счет 756516673830602841455",
    },
]


def filter_by_currency(transactions: list[dict], currency_transaction: str) -> Any:
    """Функция, возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    if transactions == []:
        yield "Список пустой!"
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_transaction:
            yield transaction


# Работа функции с пустым списком транзакций. Вывод: Список пустой! Конец списка!
# usd_transactions = filter_by_currency([], "USD")

# Работа функции по заданной валюте "EUR".
# Вывод: крайняя транзакция из списка transactions с заданной "EUR"
# и Конец списка! (т.к. в первой и второй транзакциях не найдено "EUR", там "USD")
# usd_transactions = filter_by_currency(transactions, "EUR")

# Работа функции по заданной валюте "USD".
# Вывод: первые две транзакции из списка transactions с заданной "USD"
# и Конец списка! (т.к. в третей транзакции не найдено "USD", там "EUR")
# usd_transactions = filter_by_currency(transactions, "USD")

# Работа функции по заданной отсутствующей валюте "RUS".
# Вывод: Конец списка! (т.к. во всем списке transactions не найдена заданная валюта "RUS".)
# usd_transactions = filter_by_currency(transactions, "RUS")

# try:
#     for _ in range(3):
#         print(next(usd_transactions))
# except StopIteration:
#     print("Конец списка!")  # Выводится, если закончились все тразакции в списке или отсутсвуют вовсе.


def transaction_descriptions(transactions: list[dict]) -> Any:
    """Функция, принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    if transactions == []:
        yield "Список пустой!"
    for transaction in transactions:
        try:
            yield transaction["description"]
        except Exception:
            yield "Нет информации о транзакции!"


# Работа функции с пустым списком транзакций. Вывод: Список пустой! Конец списка!
# descriptions = transaction_descriptions([])

# Корректные описания для каждой транзакции.
# descriptions = transaction_descriptions(transactions)

# Работа функции с различным количеством входных транзакций, одна (несколько или все) из которых БЕЗ описания.
# Вывод: Перевод организации Нет информации о транзакции! Перевод со счета на счет
# descriptions = transaction_descriptions(transactions_for_func_descriptions)
# try:
#     for _ in range(5):
#         print(next(descriptions))
# except StopIteration:
#     print("Конец списка!")


def card_number_generator(start: int = 1, stop: int = 5) -> Iterator[Any]:
    """Генератор, который принимает начальное и конечное значения для генерации диапазона номеров."""
    if not (1 <= start <= stop <= 9999999999999999):
        raise ValueError("Некорректный диапазон номеров карт")

    for number in range(start, stop + 1):
        card_number = "{:016d}".format(number)
        formatted_card_number = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number


# ValueError: Некорректный диапазон номеров карт (Ошибка: stop больше 9999999999999999)
# for card_number in card_number_generator(9999999999999996, 99999999999999990):
#     print(card_number)

# ValueError: Некорректный диапазон номеров карт (Ошибка: start равен 0)
# for card_number in card_number_generator(0, 15):
#     print(card_number)

# ValueError: Некорректный диапазон номеров карт (Ошибка: start больше stop)
# for card_number in card_number_generator(15, 5):
#     print(card_number)

# # Корректный вывод генерации от 1 до 5 (0000 0000 0000 0001 до 0000 0000 0000 0005)
# for card_number in card_number_generator(1, 5):
#     print(card_number)

# Корректный вывод генерации от 1234 до 1234 (0000 0000 0000 1234)
# for card_number in card_number_generator(1234, 1234):
#     print(card_number)

# Корректный вывод генерации от 1234567890123456 до 1234567890123456 (1234 5678 9012 3456)
# for card_number in card_number_generator(1234567890123456, 1234567890123456):
#     print(card_number)

# Корректный вывод генерации от 9999 9999 9999 9996 до 9999999999999999
# (Вывод: 9999 9999 9999 9996 до 9999 9999 9999 9999)
# for card_number in card_number_generator(9999999999999996, 9999999999999999):
#     print(card_number)
