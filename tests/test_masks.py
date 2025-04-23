import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896060", "7000 79** **60 60"),
        ("7000792289606", "7000 79** *960 6"),
        ("7000792289606361000", "7000 79** **** ***1 000"),
    ],
)
def test_get_mask_card_number(number: str, expected_result: str) -> None:
    """Тестирование правильности маскирования номера счета.
    Проверка работы функции на различных входных форматах номеров карт (15 для American Express),
    включая граничные случаи и нестандартные длины номеров (max - 19, min - 13)."""
    assert get_mask_card_number(number) == expected_result


@pytest.mark.parametrize("number_absent, expected_result_mask_card_number_absent", [("", "ValueError")])
def test_get_mask_card_number_absent(number_absent: str, expected_result_mask_card_number_absent: str) -> None:
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""
    with pytest.raises(ValueError):
        get_mask_card_number(number_absent) == expected_result_mask_card_number_absent


@pytest.mark.parametrize(
    "number_bank_account, expected_result_mask_bank_account",
    [("73654108430135874305", "**4305"), ("40817810538091310419", "**0419"), ("13500000010000009330", "**9330")],
)
def test_get_mask_account(number_bank_account: str, expected_result_mask_bank_account: str) -> None:
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(number_bank_account) == expected_result_mask_bank_account


@pytest.mark.parametrize(
    "incorrect_bank_account, expected_result_by_incorrect_bank_account",
    [("874305", "ValueError"), ("135", "ValueError"), ("4081781050000038091310419", "ValueError"), ("", "ValueError")],
)
def test_get_mask_by_incorrect_bank_account(
    incorrect_bank_account: str, expected_result_by_incorrect_bank_account: str
) -> None:
    """Проверка работы функции с различными форматами и длинами номеров счетов.
    Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины."""
    with pytest.raises(ValueError):
        get_mask_account(incorrect_bank_account) == expected_result_by_incorrect_bank_account
