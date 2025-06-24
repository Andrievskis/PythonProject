from collections import Counter
from typing import Any

import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.fixture
def bank_opirations_list() -> list[dict[str, int | str]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 789900065, "state": "FINISHED", "date": "2020-07-03T18:35:29.512964"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected_result",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("FINISHED", [{"id": 789900065, "state": "FINISHED", "date": "2020-07-03T18:35:29.512964"}]),
    ],
)
def test_filter_by_state(
    bank_opirations_list: list[dict[str, int | str]], state: str, expected_result: list[dict[str, int | str]]
) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state."""
    result = filter_by_state(bank_opirations_list, state)
    assert result == expected_result


@pytest.mark.parametrize(
    "expected_result_by_state_by_default",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    ],
)
def test_filter_by_state_by_default(
    bank_opirations_list: list[dict[str, int | str]], expected_result_by_state_by_default: list[dict[str, int | str]]
) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state по умолчанию."""
    result_by_state_by_default = filter_by_state(bank_opirations_list)
    assert result_by_state_by_default == expected_result_by_state_by_default


@pytest.mark.parametrize(
    "state_not_in_dictionary, expected_result_by_state_not_in_dictionary",
    [
        ("FIN", "ValueError"),
        ("ESCAP", "ValueError"),
        ("123456", "ValueError"),
        ("", "ValueError"),
        ("aabccdd", "ValueError"),
    ],
)
def test_filter_by_state_not_in_dictionary(
    bank_opirations_list: list[dict[str, int | str]],
    state_not_in_dictionary: str,
    expected_result_by_state_not_in_dictionary: str,
) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом
    state в списке."""
    with pytest.raises(ValueError):
        result_by_state_not_in_dictionary = filter_by_state(bank_opirations_list, state_not_in_dictionary)
        result_by_state_not_in_dictionary == expected_result_by_state_not_in_dictionary


@pytest.mark.parametrize(
    "state_invalid_type_data, expected_result_by_state_invalid_type_data",
    [
        (128400, "TypeError"),
        (9876543, "TypeError"),
        (576.8, "TypeError"),
        (True, "TypeError"),
        (False, "TypeError"),
    ],
)
def test_filter_by_state_invalid_type_data(
    bank_opirations_list: list[dict[str, int | str]],
    state_invalid_type_data: str,
    expected_result_by_state_invalid_type_data: str,
) -> None:
    """Проверка работы функции при некорректном типе данных state."""
    with pytest.raises(TypeError):
        result_by_state_invalid_type_data = filter_by_state(bank_opirations_list, state_invalid_type_data)
        result_by_state_invalid_type_data == expected_result_by_state_invalid_type_data


@pytest.mark.parametrize(
    "reverse_decreasing_increase, expected_sort_by_date_decreasing_increase",
    [
        (
            True,
            [
                {"id": 789900065, "state": "FINISHED", "date": "2020-07-03T18:35:29.512964"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 789900065, "state": "FINISHED", "date": "2020-07-03T18:35:29.512964"},
            ],
        ),
    ],
)
def test_sort_by_date_decreasing_and_increase(
    bank_opirations_list: list[dict[str, int | str]],
    reverse_decreasing_increase: bool,
    expected_sort_by_date_decreasing_increase: list[dict[str, int | str]],
) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""
    result_decreasing_increase = sort_by_date(bank_opirations_list, reverse_decreasing_increase)
    assert result_decreasing_increase == expected_sort_by_date_decreasing_increase


@pytest.mark.parametrize(
    "expected_sort_by_date_decreasing_increase",
    [
        [
            {"id": 789900065, "state": "FINISHED", "date": "2020-07-03T18:35:29.512964"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    ],
)
def test_sort_by_date_decreasing_increase(
    bank_opirations_list: list[dict[str, int | str]],
    expected_sort_by_date_decreasing_increase: list[dict[str, int | str]],
) -> None:
    """Тестирование сортировки списка словарей по датам по умолчанию."""
    result_decreasing_increase = sort_by_date(bank_opirations_list)
    assert result_decreasing_increase == expected_sort_by_date_decreasing_increase


@pytest.mark.parametrize(
    "reverse_any, expected_sort_by_same_date",
    [
        (
            True,
            [
                {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "ESCAPED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            False,
            [
                {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "ESCAPED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_same_date(reverse_any: bool, expected_sort_by_same_date: list[dict[str, int | str]]) -> None:
    """Проверка корректности сортировки при одинаковых датах."""
    result_sort_by_same_date = sort_by_date(
        [
            {"id": 41428829, "state": "FINISHED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "ESCAPED", "date": "2019-07-03T18:35:29.512364"},
        ],
        reverse_any,
    )
    assert result_sort_by_same_date == expected_sort_by_same_date


@pytest.mark.parametrize(
    "reverse_any_, expected_sort_by_incorrect_dates", [(True, "ValueError"), (False, "ValueError")]
)
def test_sort_by_incorrect_dates(
    reverse_any_: bool, expected_sort_by_incorrect_dates: list[dict[str, int | str]]
) -> None:
    """Тесты на работу функции с некорректными или нестандартными форматами дат."""
    with pytest.raises(ValueError):
        result_sort_by_incorrect_dates = sort_by_date(
            [
                {"id": 41428829, "state": "FINISHED", "date": "5 января"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30"},
                {"id": 594226727, "state": "CANCELED", "date": ""},
                {"id": 615064591, "state": "ESCAPED", "date": "2018-10"},
            ],
            reverse_any_,
        )
        result_sort_by_incorrect_dates == expected_sort_by_incorrect_dates


@pytest.fixture
def data_list() -> list[dict]:
    return [
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
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 756516673830602841455",
        },
    ]


@pytest.mark.parametrize(
    "search_string, expected_result",
    [
        (
            "перевод организации",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
        (
            "Перевод со СЧЕТА на счет",
            [
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
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 756516673830602841455",
                },
            ],
        ),
    ],
)
def test_process_bank_search(data_list: list[dict], search_string: str, expected_result: list[dict]) -> None:
    """Тест на корректную работу функции (и без учета регистра)."""
    result = process_bank_search(data_list, search_string)
    assert result == expected_result


@pytest.mark.parametrize(
    "search_string_empty, expected_result_",
    [
        (
            "",
            [
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
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 756516673830602841455",
                },
            ],
        )
    ],
)
def test_process_bank_search_empty(
    data_list: list[dict], search_string_empty: str, expected_result_: list[dict]
) -> None:
    """Тест на корректную работу функции с пустой строкой поиска."""
    result_ = process_bank_search(data_list, search_string_empty)
    assert result_ == expected_result_


@pytest.mark.parametrize("search_string_unknown_operation, expected", [("операция", [])])
def test_process_bank_search_unknown_operation(
    data_list: list[dict], search_string_unknown_operation: str, expected: list
) -> None:
    """Тест на корректную работу функции с неизвестной операцией."""
    result = process_bank_search(data_list, search_string_unknown_operation)
    assert result == expected


@pytest.mark.parametrize(
    "categories, expected_result_categories",
    [
        (
            [
                "Перевод организации",
                "Открытие вклада",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод с карты на счет",
            ],
            {"Перевод организации": 1, "Перевод со счета на счет": 2},
        )
    ],
)
def test_process_bank_operations(categories: list, expected_result_categories: Counter, data_list: list[dict]) -> None:
    """Тест на корректную работу функции подсчета количества банковских операций определенного типа.
    С использованием Counter."""
    result_categories = process_bank_operations(data_list, categories)
    assert result_categories == expected_result_categories


@pytest.mark.parametrize(
    "categories_error, expected_error",
    [
        ("Перевод организации", TypeError),
        (28754578, TypeError),
        ({"Перевод организации", "Открытие вклада"}, TypeError),
    ],
)
def test_process_bank_operations_error(data_list: list[dict], categories_error: Any, expected_error: str) -> None:
    """Тест на обработку ошибки, в случе передачи (categories) некорректного типа данных."""
    with pytest.raises(TypeError):
        result_categories_error = process_bank_operations(data_list, categories_error)
        assert result_categories_error == expected_error
