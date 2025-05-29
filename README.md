# Проект "Банковские операции"

## Описание:

_Модуль masks содержит две функции: get_mask_card_number функция маскирования номера карты и get_mask_account функция
маскирования номера счета. Модуль widget содержит две функции: mask_account_card функция, обрабатывающая информацию
о картах и счетах и get_date функция для изменения (заданного по условию) формата даты. Модуль processing содержит две
функции: filter_by_state функция фильтрации списка словарей по заданному статусу
state и sort_by_date функция сортировки списка словарей по датам в порядке убывания и возрастания._
Проект содержит тестовые модули test_masks, test_widget, test_processing для надежности и качества кода. Каждый  
модуль содержит тестирование на правильность использования функций данного проекта, что помогает поддерживать высокий
уровень качества данного проекта.
_Модуль generators содержать функции для работы с массивами транзакций.
Этот модуль содержит функции, реализующие генераторы для обработки данных. Функция filter_by_currency возвращает
итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной. Генератор
transaction_descriptions принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
Генератор card_number_generator выдает номера банковских карт в определенном формате.
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Также имеется тестовый модуль test_generators, к модулю generators, для надежности и качества кода.
Добавлен модуль decorators, он содержит декоратор log, который автоматически логирует начало и конец выполнения
функции, а также ее результаты или возникшие ошибки. Декоратор принимает необязательный аргумент filename,
который определяет, куда будут записываться логи (в файл или в консоль)._

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
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import log
```

Пример использования get_mask_card_number:

```
mask_card_number = get_mask_card_number("7000792289606361000")
```

Пример использования get_mask_account:

```
mask_account = get_mask_account("70007922896063610000")
```

Пример использования mask_account_card:

```
mask_account = mask_account_card("Счет 73654108430135874305")
mask_card = mask_account_card("Visa Platinum 7000792289606361")
mask_card_ = mask_account_card("Maestro 7000792289606361")
```

Пример использования get_date:

```
my_date = get_date("2024-03-11T02:26:18.671407")
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

Пример использования filter_by_currency:

```
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
```

Пример использования transaction_descriptions:

```
for description in transaction_descriptions(transactions):
    print(description)
```

Пример использования card_number_generator:

```
for card_number in card_number_generator(1, 15):
    print(card_number)
```

Пример использования декоратора log когда будут записываться логи в консоль:

```
@log()
def my_function(x: int, y: int) -> int:
    return x + y
    
my_function(1, 3)
```

Пример использования декоратора log когда будут записываться логи в файл mylog.txt:

```
@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
   return x + y

my_function(1, 3)
```
