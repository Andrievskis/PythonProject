import csv
from typing import Any

import pandas as pd


def transaction_read_csv(file_path_csv: Any) -> Any:
    """Функция для считывания финансовых операций из CSV."""
    try:
        with open(file_path_csv, encoding="utf-8") as file_csv:
            reader_csv = list(csv.DictReader(file_csv, delimiter=";"))
            return reader_csv
    except (FileNotFoundError, Exception) as e:
        return f"Произошла ошибка {e}"


# print(transaction_read_csv('transactions.csv'))
# print(transaction_read_csv('/Users/anastasiaandreeva/PycharmProjects/PythonProject/data/transactions.csv'))


def transaction_read_excel(file_path_excel: Any) -> Any:
    """Функция для считывания финансовых операций из Excel."""
    try:
        reader_excel = (pd.read_excel(file_path_excel)).to_dict(orient="records")
        return reader_excel
    except (FileNotFoundError, Exception) as e:
        return f"Произошла ошибка: {e}"


# print(transaction_read_excel('transactions_excel.xlsx'))
# print(transaction_read_excel('/Users/anastasiaandreeva/PycharmProjects/PythonProject/data/transactions_excel.xlsx'))
