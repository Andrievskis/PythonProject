# Проект "Банковские операции"

## Описание:

Проект содержит две функции, одна из которых помогает отфильтровать положение операций (выполненный/отмененный) и выдать их пользователю, 
по умолчанию - выполненный. Вторая функция сортирует дату операций и выдает данные по возрастанию/убыванию даты. По умолчанию - убывание.

## Установка:

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Andrievskis/PythonProject.git
   ```
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
## Использование:

Примеры использования функций:
```
from src.processing import filter_by_state, sort_by_date
```

Пример использования filter_by_state:
```
bank_operations = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
executed_operations = filter_by_state(bank_operations)
```

Пример использования sort_by_date:
```
sorted_operations = sort_by_date(bank_operations)
```
