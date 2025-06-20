from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.reader import transaction_read_csv, transaction_read_excel


def test_transaction_read_csv() -> None:
    """Тест на корректную работу функции, считывания финансовых операций из CSV."""
    test_csv_data: str = "id;amount;date\n1;100.00;2025-06-16\n2;200.00;2025-06-17"
    with patch("builtins.open", new_callable=mock_open, read_data=test_csv_data):
        result = transaction_read_csv("test.csv")

    expected = [
        {"id": "1", "amount": "100.00", "date": "2025-06-16"},
        {"id": "2", "amount": "200.00", "date": "2025-06-17"},
    ]

    assert result == expected


@patch("builtins.open", side_effect=FileNotFoundError)
def test_transaction_read_csv_not_found(mock_file: Any) -> None:
    """Тест на корректную работу функции, где файл не найден. Ошибка FileNotFoundError."""
    result = transaction_read_csv("non_file.csv")

    assert result == "Произошла ошибка " in result


@patch("builtins.open", side_effect=Exception)
def test_transaction_read_csv_error(mock_file: Any) -> None:
    """Тест на корректную работу функции с некорректными данными. Ошибка Exception."""
    result = transaction_read_csv("invalid_file.csv")

    assert result == "Произошла ошибка " in result


@patch("pandas.read_excel")
def test_transaction_read_excel(mock_read_excel: Any) -> None:
    """Тест на корректную работу функции, считывания финансовых операций из Excel."""
    mock_read_excel.return_value = pd.DataFrame(
        {"id": [1, 2], "amount": [100.00, 200.00], "date": ["2025-06-16", "2025-06-17"]}
    )

    result = transaction_read_excel("test.xlsx")

    expected = [{"id": 1, "amount": 100.00, "date": "2025-06-16"}, {"id": 2, "amount": 200.00, "date": "2025-06-17"}]

    assert result == expected


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_transaction_read_excel_not_found(mock_read_excel: Any) -> None:
    """Тест на корректную работу функции, где файл не найден. Ошибка FileNotFoundError."""
    result = transaction_read_excel("non_existent.xlsx")

    assert "Произошла ошибка" in result


@patch("pandas.read_excel", side_effect=Exception)
def test_transaction_read_excel_error(mock_read_excel: Any) -> None:
    """Тест на корректную работу функции с некорректными данными. Ошибка Exception."""
    result = transaction_read_excel("invalid.xlsx")

    assert "Произошла ошибка" in result
