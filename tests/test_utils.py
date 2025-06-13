import unittest
from unittest.mock import patch, mock_open
import json
from src.utils import operations_file
from typing import List, Dict, Any


@patch("builtins.open", new_callable=mock_open)
def test_valid_json_list(mock_file: Any) -> None:
    """Тест на корректную работу функции, где указан правильный путь до файла
    и файл содержит корректную информацию в виде списка словарей."""
    test_data: str = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    mock_file.return_value.read.return_value = test_data
    result: List[Dict[str, Any]] = operations_file("test_path")

    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_file.assert_called_once_with("test_path", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open)
def test_invalid_json_type(mock_file: Any) -> None:
    """Тест на корректную работу функции, где указан правильный путь до файла,
    но файл содержит некорректную информацию в виде словаря."""
    test_data: str = json.dumps({"id": 1, "amount": 100})
    mock_file.return_value.read.return_value = test_data
    result: List[Dict[str, Any]] = operations_file("test_path")

    assert result == []
    mock_file.assert_called_once_with("test_path", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open)
def test_empty_json(mock_file: Any) -> None:
    """Тест на корректную работу функции, где указан правильный путь до файла,
    но файл пустой."""
    mock_file.return_value.read.return_value = ""
    result: List[Dict[str, Any]] = operations_file("test_path")

    assert result == []
    mock_file.assert_called_once_with("test_path", "r", encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file: Any) -> None:
    """Тест на корректную работу функции, где файл не найден. Ошибка FileNotFoundError."""
    result: List[Dict[str, Any]] = operations_file("non_existent_path")

    assert result == []
    mock_file.assert_called_once_with("non_existent_path", "r", encoding="utf-8")


@patch("builtins.open", side_effect=json.JSONDecodeError("", "", 0))
def test_json_decode_error(mock_file: Any) -> None:
    """Тест на корректную работу функции, когда не соответсвует формату JSON. Ошибка JSONDecodeError."""
    result: List[Dict[str, Any]] = operations_file("invalid_json_path")

    assert result == []
    mock_file.assert_called_once_with("invalid_json_path", "r", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
