# from src.utils import operations_file, path_to_file_operations
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_conversion(transaction: dict) -> Any:
    """Функция конвертации валюты из USD в рубли возвращает сумму транзакции
    в рублях, тип данных float."""
    if transaction.get("operationAmount"):
        amount = (transaction["operationAmount"]).get("amount")
        currency = (transaction["operationAmount"]["currency"]).get("code")
        ruble = "RUB"
        if amount is None or currency is None:
            return None

        if currency == ruble:
            return float(amount)
        elif currency != ruble:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={ruble}&from={currency}&amount={amount}"
            headers = {"apikey": os.getenv("API_KEY")}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return round(float(response.json()["result"]), 2)
            elif response.status_code == 429:
                return f"Ошибка {response.status_code}: Превышен лимит запросов."
            elif response.status_code == 524:
                return f"Ошибка {response.status_code}: Время ожидания истекло."
            else:
                return f"Произошла ошибка: {response.status_code}"
    return "Нет данных в словаре."


# цикл для обработки каждой транзакции поочередно из operations.json
# (с обращением к модулю utils.py, необходимо разкомментировать импорт)
# for i in operations_file(path_to_file_operations):
#     print(get_conversion(i))
