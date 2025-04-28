import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number_account_or_card, exepted_number_account_or_card",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_and_card(number_account_or_card: str, exepted_number_account_or_card: str) -> None:
    """Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки
    в зависимости от типа входных данных (карта или счет).
    Также параметризованные тесты с разными типами карт и счетов для проверки универсальности функции."""
    assert mask_account_card(number_account_or_card) == exepted_number_account_or_card


@pytest.mark.parametrize(
    "incorrect_number_account_or_card, expected_result_number_account_or_card",
    [(7000792289606361, "ValueError"), ("Счет", "ValueError"), (None, "ValueError"), ("", "ValueError")],
)
def test_mask_incorrect_account_and_card(
    incorrect_number_account_or_card: str, expected_result_number_account_or_card: str
) -> None:
    """Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам."""
    with pytest.raises(ValueError):
        mask_account_card(incorrect_number_account_or_card) == expected_result_number_account_or_card


@pytest.mark.parametrize("input_date, expected_date", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(input_date: str, expected_date: str) -> None:
    """Тестирование правильности преобразования даты."""
    assert get_date(input_date) == expected_date


@pytest.mark.parametrize(
    "incorrect_date, expected_result_date",
    [
        ("2024-03-11", "ValueError"),
        ("", "ValueError"),
        ("2024/07/03T18:35:29", "ValueError"),
        ("03-07-2025T18:35:29", "ValueError"),
    ],
)
def test_get_incorrect_dat(incorrect_date: str, expected_result_date: str) -> None:
    """Проверка работы функции на различных входных
    форматах даты, включая граничные случаи и нестандартные строки с датами.
    Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата."""
    with pytest.raises(ValueError):
        get_date(incorrect_date) == expected_result_date
