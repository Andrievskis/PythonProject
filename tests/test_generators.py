from typing import Any, Callable, Iterator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions_list() -> list[dict]:
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


@pytest.fixture
def transactions_for_func_descriptions() -> list[dict]:
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


@pytest.mark.parametrize(
    "currency_transaction, expected_result_transaction",
    [
        (
            "USD",
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
            ],
        ),
        (
            "EUR",
            [
                {
                    "id": 167764268,
                    "state": "EXECUTED",
                    "date": "2020-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 756516673830602841455",
                }
            ],
        ),
    ],
)
def test_filter_by_currency(
    transactions_list: list[dict], currency_transaction: str, expected_result_transaction: list[dict]
) -> None:
    """Проверка, что функция корректно фильтрует транзакции по заданной валюте."""
    result_by_currency = filter_by_currency(transactions_list, currency_transaction)
    assert list(result_by_currency) == list(expected_result_transaction)


@pytest.mark.parametrize(
    "currency_transaction_for_empty_list, expected_result_with_empty_list", [("USD", ["Список пустой!"])]
)
def test_filter_by_currency_with_empty_list(
    currency_transaction_for_empty_list: str, expected_result_with_empty_list: list
) -> None:
    """Проверка работы функции с пустым списком транзакций."""
    result_currency_with_empty_list = list(filter_by_currency([], currency_transaction_for_empty_list))
    assert result_currency_with_empty_list == expected_result_with_empty_list


@pytest.mark.parametrize(
    "expected_result_descriptions", [["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]]
)
def test_transaction_descriptions(transactions_list: list[dict], expected_result_descriptions: list) -> None:
    """Проверка работы функции когда функция возвращает корректные описания для каждой транзакции."""
    result_transaction_descriptions = transaction_descriptions(transactions_list)
    assert list(result_transaction_descriptions) == list(expected_result_descriptions)


@pytest.mark.parametrize("expected_with_empty_list", [["Список пустой!"]])
def test_transaction_descriptions_with_empty_list(expected_with_empty_list: list) -> None:
    """Проверка работы функции описания операций с пустым списком транзакций."""
    result_descriptions_with_empty_list = list(transaction_descriptions([]))
    assert result_descriptions_with_empty_list == expected_with_empty_list


@pytest.mark.parametrize(
    "expected_result_descriptions_",
    [["Перевод организации", "Нет информации о транзакции!", "Перевод со счета на счет"]],
)
def test_transaction_descriptions_(
    transactions_for_func_descriptions: list[dict], expected_result_descriptions_: list
) -> None:
    """Проверка работы функции когда функция возвращает корректные описания для каждой транзакции.
    С учетом отсутствия информации в словаре о транзакции."""
    result_transaction_descriptions_ = transaction_descriptions(transactions_for_func_descriptions)
    assert list(result_transaction_descriptions_) == list(expected_result_descriptions_)


@pytest.fixture
def card_generator() -> Callable[[int, int], Iterator[Any]]:
    return card_number_generator


@pytest.mark.parametrize(
    "start_number_generator, stop_number_generator, expected_card_number_generator",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (1234, 1234, ["0000 0000 0000 1234"]),
        (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
    ],
)
def test_card_number_generator(
    card_generator: Callable[[int, int], Iterator[Any]],
    start_number_generator: int,
    stop_number_generator: int,
    expected_card_number_generator: Callable[[int, int], Iterator[Any]],
) -> None:
    """Проверка работы функции, что генератор выдает правильные номера карт в заданном диапазоне."""
    assert list(card_generator(start_number_generator, stop_number_generator)) == expected_card_number_generator


@pytest.mark.parametrize(
    "start_range, stop_range,expected_len_card_number_generator_range",
    [(1, 8, 8), (1234, 1234, 1), (1234567890123454, 1234567890123456, 3)],
)
def test_card_number_generator_range(
    card_generator: Callable[[int, int], Iterator[Any]],
    start_range: int,
    stop_range: int,
    expected_len_card_number_generator_range: Callable[[int, int], Iterator[Any]],
) -> None:
    """Проверка работы функции, что генератор корректно обрабатывает
    крайние значения диапазона и правильно завершает генерацию."""
    result_card_number_generator_range = list(card_generator(start_range, stop_range))
    assert len(result_card_number_generator_range) == expected_len_card_number_generator_range


@pytest.mark.parametrize(
    "start_invalid_values, stop_invalid_values, expected_invalid_values",
    [(0, 5, "ValueError"), (6, 5, "ValueError"), (9999999999999996, 99999999999999990, "ValueError")],
)
def test_card_number_generator_invalid_values(
    card_generator: Callable[[int, int], Iterator[Any]],
    start_invalid_values: int,
    stop_invalid_values: int,
    expected_invalid_values: str,
) -> None:
    """Проверка работы функции, что генератор корректно обрабатывает
    некорректных значения start, stop."""
    with pytest.raises(ValueError):
        res = list(card_generator(start_invalid_values, stop_invalid_values))
        assert res == list(expected_invalid_values)
