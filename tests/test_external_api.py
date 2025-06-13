import unittest
from typing import Any, Dict
from unittest.mock import patch
from src.external_api import get_conversion

# Тестовые данные
transaction_rub: Dict[str, Dict[str, Any]] = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

transaction_usd: Dict[str, Dict[str, Any]] = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

transaction_invalid: Dict[str, Dict[str, Any]] = {"operationAmount": {"amount": None, "currency": {"code": None}}}

transaction_empty: Dict = {}


@patch("requests.get")
def test_get_conversion_rub_to_rub(mock_get: Any) -> None:
    """Тест на корректную конвертацию из RUB в RUB."""
    result = get_conversion(transaction_rub)
    assert result == 100.0


@patch("requests.get")
def test_get_conversion_usd_to_rub(mock_get: Any) -> None:
    """Тест на конвертацию из USD в RUB с успешным ответом API."""
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9500.0}

    result = get_conversion(transaction_usd)
    assert result == 9500.0


@patch("requests.get")
def test_get_conversion_missing_data(mock_get: Any) -> None:
    """Тест на обработку транзакции с отсутствующими данными (если один из словарей пустой)."""
    result = get_conversion(transaction_empty)
    assert result == "Нет данных в словаре."


@patch("requests.get")
def test_get_conversion_api_error_429(mock_get: Any) -> None:
    """Тест на обработку ошибки 429 от API."""
    mock_response = mock_get.return_value
    mock_response.status_code = 429

    result = get_conversion(transaction_usd)
    assert result == "Ошибка 429: Превышен лимит запросов."


@patch("requests.get")
def test_get_conversion_api_error_524(mock_get: Any) -> None:
    """Тест на обработку ошибки 524 от API."""
    mock_response = mock_get.return_value
    mock_response.status_code = 524

    result = get_conversion(transaction_usd)
    assert result == "Ошибка 524: Время ожидания истекло."


@patch("requests.get")
def test_get_conversion_api_unknown_error(mock_get: Any) -> None:
    """Тест на обработку неизвестной ошибки API."""
    mock_response = mock_get.return_value
    mock_response.status_code = 500

    result = get_conversion(transaction_usd)
    assert result == "Произошла ошибка: 500"


# Запуск всех тестов
if __name__ == "__main__":
    unittest.main()
