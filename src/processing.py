import re
from collections import Counter
from typing import Any

from src.widget import get_date

bank_operations_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 789900065, "state": "FINISHED", "date": "2020-07-03T18:35:29.512964"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(
    bank_operations: list[dict[str, int | str]], state: str = "EXECUTED"
) -> list[dict[str, int | str]]:
    """Функция, фильтрующая положение операций (выполненный или отмененный)."""
    filter_list = [
        bank_operation
        for bank_operation in bank_operations
        if "state" in bank_operation and bank_operation["state"] == state
    ]
    if not isinstance(state, str):
        raise TypeError("Ошибка типа данных.")
    elif not filter_list:
        raise ValueError("Указанное значение не найдено в словаре.")
    return filter_list


# Фильтрации списка словарей по заданному статусу "CANCELED".
# print(filter_by_state(bank_operations_list, state="CANCELED"))


# Фильтрации списка словарей по заданному статусу "EXECUTED" - по умолчанию.
# print(filter_by_state(bank_operations_list))


def sort_by_date(users_bank_operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, сортирующая операции по дате."""
    users_bank_operations_ = list()
    for operation in users_bank_operations:
        if "date" not in operation:
            continue
        date_time = str(operation["date"])
        date = get_date(date_time)
        if date != "Incorrect date":
            users_bank_operations_.append(operation)

    sorted_processes_users_bank_operations = sorted(users_bank_operations_, key=lambda k: k["date"], reverse=reverse)

    return sorted_processes_users_bank_operations


# Сортировка по убыванию.
# print(sort_by_date(bank_operations_list))

# Сортировка по возрастанию.
# print(sort_by_date(bank_operations_list, reverse=False))


# data_list = operations_file(path_to_file_operations)
# # print(data_list)


def process_bank_search(data: list[dict], search_string: str) -> list[dict] | Any:
    """Функция для поиска в списке словарей операций по заданной строке."""
    try:
        pattern = re.compile(re.escape(search_string), re.IGNORECASE)
        filter_list_data = [data_ for data_ in data if pattern.search(data_.get("description", ""))]
        return filter_list_data
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None


# print(process_bank_search(data_list, 'перевод организации'))


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа.
    С использованием Counter из библиотеки collections."""
    category_count: Any = Counter()
    for transaction in data:
        description = transaction.get("description", "").lower()
        if isinstance(categories, list):
            for category in categories:
                if category.lower() in description:
                    category_count[category] += 1
        else:
            raise TypeError("Ошибка типа данных.")
    return dict(category_count)


# Корректный подсчета количества банковских операций определенного типа. С использованием Counter.
# print(process_bank_operations(data_list, ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет',
#                   'Перевод с карты на карту', 'Перевод с карты на счет']))
