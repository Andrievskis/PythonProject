def filter_by_state(bank_operations: list[dict[str, int | str]], state: str = 'EXECUTED') -> list[dict[str, int | str]]:
    """Функция, фильтрующая положение операций (выполненный или отмененный)."""
    bank_operations_state = []
    for bank_operation in bank_operations:
        if bank_operation['state'] == state:
            bank_operations_state.append(bank_operation)
    return bank_operations_state


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], state='CANCELED'))


def sort_by_date(users_bank_operations: list[dict[str, int | str]], reverse: bool = True) -> list[dict[str, int | str]]:
    """Функция, сортирующая дату операций по убыванию."""
    return sorted(users_bank_operations, key=lambda user_bank_operation: user_bank_operation['date'], reverse=reverse)


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
