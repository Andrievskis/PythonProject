from datetime import datetime

from typing import Any


def filter_by_state(
    bank_operations: list[dict[str, int | str]], state: str = "EXECUTED"
) -> list[dict[str, int | str]]:
    """Функция, фильтрующая положение операций (выполненный или отмененный)."""
    filter_list = [bank_operation for bank_operation in bank_operations if bank_operation["state"] == state]
    if not filter_list:
        raise ValueError("Указанное значение не найдено в словаре.")
    return filter_list


# Фильтрации списка пустого. ValueError: Указанное значение не найдено в словаре.
# print(filter_by_state([]))

# Фильтрации списка словарей по заданному (отсутствующему) статусу "CAN".
# ValueError: Указанное значение не найдено в словаре.
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ], state="CAN"
#     )
# )


# Фильтрации списка словарей по заданному статусу "CANCELED".
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         state="CANCELED",
#     )
# )


# Фильтрации списка словарей по заданному статусу "EXECUTED" - по умолчанию.
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )


def sort_by_date(users_bank_operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, сортирующая дату операций по убыванию."""
    try:
        return sorted(
            users_bank_operations,
            key=lambda user_bank_operation: datetime.strptime(user_bank_operation["date"], "%Y-%m-%dT%H:%M:%S.%f"),
            reverse=reverse,
        )
    except ValueError:
        raise ValueError("Некорректный формат даты.")


# Некорректный формат даты. ValueError("Некорректный формат даты.")
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "FINISHED", "date": "5 января"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018"},
#             {"id": 615064591, "state": "ESCAPED", "date": "2018-10"}
#         ]
#     )
# )


# Сортировка по убыванию.
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "ESCAPED", "date": "2018-10-14T08:21:33.419441"}
#         ]
#     )
# )

# Сортировка по возрастанию.
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "ESCAPED", "date": "2018-10-14T08:21:33.419441"}
#         ], reverse=False
#     )
# )


# Сортировка при одинаковых датах.
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 615064591, "state": "ESCAPED", "date": "2019-07-03T18:35:29.512364"},
#         ]
#     )
# )
