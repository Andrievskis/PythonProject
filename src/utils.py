import json
import logging
from typing import Any

logger = logging.getLogger("utils_log")
file_handler = logging.FileHandler(
    "/Users/anastasiaandreeva/PycharmProjects/PythonProject/logs/utils.log", "w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def operations_file(path_to_file: Any) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        logger.warning("Файл должен содержать список словарей!")
        with open(path_to_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            logger.info(f"Список с данными о финансовых транзакциях {data}")
            return data
        else:
            logger.error(f"Данные {data} должны быть списком словарей.")
            raise ValueError(f"Файл {data} не является списком словарей.")

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        return []
    finally:
        logger.info("Завершение работы функции.")


# Путь к существующему файлу
path_to_file_operations = "/Users/anastasiaandreeva/PycharmProjects/PythonProject/data/operations.json"
# print(operations_file(path_to_file_operations))
