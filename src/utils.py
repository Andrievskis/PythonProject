import json
from typing import Any


def operations_file(path_to_file: Any) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        with open(path_to_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            return data
        else:
            raise ValueError("Данные должны быть списком словарей.")

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


# Путь к существующему файлу
path_to_file_operations = "/Users/anastasiaandreeva/PycharmProjects/PythonProject/data/operations.json"
print(operations_file(path_to_file_operations))

# Путь к несуществующему файлу
path_to_file_operations_not_found = "/operations.json"
print(operations_file(path_to_file_operations_not_found))
