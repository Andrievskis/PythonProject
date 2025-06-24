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
который определяет, куда будут записываться логи (в файл или в консоль).
Модуль utils содержит функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей
с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
функция возвращает пустой список.
Модуль external_api содержит функцию, конвертации валюты из USD и EUR в рубли принимает на вход словарь с данными
о транзакции. Функция конвертации валюты из USD и EUR в рубли возвращает сумму транзакции (ключ amount) в рублях,
тип данных float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего
курса валют и конвертации суммы операции в рубли. Очень важно: для работы с API необходимо настроить
файл `.env` с токенами доступа.
В модулях utils и masks реализованна запись логов в файл (использование библиотеки logging). Логи записываются в
папку logs в корне проекта. Файлы логов имеют расширение .log в следующем формате: метка времени, название модуля,
уровень серьезности и сообщение, описывающее событие или ошибку, которые произошли.
Лог перезаписывается при каждом запуске приложения.
Библиотека logging используется для создания структурированных и полезных логов с минимальными усилиями.
Логи помогут быстро понять, что происходит в приложении, и упростят процесс отладки и мониторинга.
Модуль reader содержит функции для считывания финансовых операций из CSV и из Excel.
Модуль processing дополнен функциями для поиска в списке словарей операций по заданной строке и для подсчета количества
банковских операций определенного типа. С использованием Counter из библиотеки collections.
Реализован модуль main, который отвечает за основную логику проекта и связывает функциональности между собой._

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
from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import log
from src.utils import operations_file
from src.external_api import get_conversion
from src.reader import transaction_read_csv, transaction_read_excel
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

Пример использования operations_file:

```
path_to_file_operations = ".../operations.json"

print(operations_file(path_to_file_operations))

```

Пример использования get_conversion:

``` 
transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    
print(get_conversion(transaction))
```

Пример использования transaction_read_csv:

```
file_path_csv = '.../data/transactions.csv'
print(transaction_read_csv(file_path_csv))

```

Пример использования transaction_read_excel:

```
file_path_excel = '.../data/transactions_excel.xlsx'
print(transaction_read_excel(file_path_excel))

```
Пример использования process_bank_search:

```
path_to_file_operations = ".../operations.json"
data_list = operations_file(path_to_file_operations)

print(process_bank_search(data_list, 'перевод организации'))

```

Пример использования process_bank_operations:

```
path_to_file_operations = ".../operations.json"
data_list = operations_file(path_to_file_operations)

print(process_bank_operations(data_list, ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет',
                  'Перевод с карты на карту', 'Перевод с карты на счет']))

```

## Пример работы main:
Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Пользователь: 1

Программа: Для обработки выбран JSON-файл.
Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Пользователь: EXECUTED

Программа: Операции отфильтрованы по статусу "EXECUTED"
Программа: Отсортировать операции по дате? Да/Нет

Пользователь: да

Программа: Отсортировать по возрастанию или по убыванию? 

Пользователь: по возрастанию/по убыванию

Программа: Выводить только рублевые транзакции? Да/Нет

Пользователь: да

Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет

Пользователь: да/нет

Программа: Распечатываю итоговый список транзакций...

Программа: 
Всего банковских операций в выборке: 4

08.12.2019 Открытие вклада 
Счет **4321
Сумма: 40542 руб. 

12.11.2019 Перевод с карты на карту
MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
Сумма: 130 USD

18.07.2018 Перевод организации 
Visa Platinum 7492 65** **** 7202 -> Счет **0034
Сумма: 8390 руб.

03.06.2018 Перевод со счета на счет
Счет **2935 -> Счет **4321
Сумма: 8200 EUR

## Настройка файла .env:

_Для работы с внешними API необходимо создать файл `.env` в корне проекта и добавить в него следующие переменные
окружения:_

```
API_KEY=ваш_ключ_доступа
API_URL=https://api.example.com
```

_Убедитесь, что файл `.env` добавлен в `.gitignore`, чтобы избежать случайного попадания конфиденциальной
информации в репозиторий._
