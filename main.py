from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date
from src.reader import transaction_read_csv, transaction_read_excel
from src.utils import operations_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """Отвечает за основную логику проекта и связывает функциональности между собой."""
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    user_input = ""
    while user_input not in ["1", "2", "3"]:
        print("1. Получить информацию о транзакциях из JSON-файла.")
        print("2. Получить информацию о транзакциях из CSV-файла.")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        user_input = input("Пользователь: ")
    transactions_data = []
    match user_input:
        case "1":
            print("Программа: Для обработки выбран JSON-файл.")
            transactions_data = operations_file(
                "/Users/anastasiaandreeva/PycharmProjects/PythonProject/data/operations.json"
            )
        case "2":
            print("Программа: Для обработки выбран CSV-файл.")
            transactions_data = transaction_read_csv(
                "/Users/anastasiaandreeva/PycharmProjects/PythonProject/data/transactions.csv"
            )
        case "3":
            print("Программа: Для обработки выбран XLSX-файл.")
            transactions_data = transaction_read_excel(
                "/Users/anastasiaandreeva/PycharmProjects/PythonProject/data/transactions_excel.xlsx"
            )

    while 1:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.")
        user_input = input("\nПользователь: ").upper()
        if user_input.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print("Программа: Статус операции '{}' недоступен.".format(user_input))
        else:
            state = user_input.upper()
            print(f"Программа: Операции отфильтрованы по статусу {state}")
            break
    transactions_data = filter_by_state(transactions_data, state)

    user_input = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ")
    if user_input.lower() == "да":
        user_input = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ")
        if user_input.lower() == "по возрастанию":
            transactions_data = sort_by_date(transactions_data, False)
        elif user_input.lower() == "по убыванию":
            transactions_data = sort_by_date(transactions_data)

    user_input = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ")
    if user_input.lower() == "да":
        transactions_data = filter_by_currency(transactions_data, "RUB")

    do_filter_by_description = 0
    user_input = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    )
    if user_input.lower() == "да":
        do_filter_by_description = 1

    if do_filter_by_description:
        user_input = input("Программа: Укажите слово.\nПользователь:  ").lower()
        transactions_data = process_bank_search(transactions_data, user_input.lower())
    else:
        transactions_data = process_bank_search(transactions_data, "")

    grouped_transactions = process_bank_operations(
        transactions_data,
        [
            "Перевод организации",
            "Открытие вклада",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод с карты на счет",
        ],
    )
    operations_count = sum(v for k, v in grouped_transactions.items())
    print("Программа: Распечатываю итоговый список транзакций...")
    print("Программа:\nВсего банковских операций в выборке:", operations_count)
    for transaction in transactions_data:
        if "operationAmount" in transaction:
            try:
                print(f"{get_date(transaction['date'])} {transaction['description']}")
                print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
                print(
                    f"Сумма: {transaction['operationAmount']['amount']} "
                    f"{transaction['operationAmount']['currency']['name']}"
                )
            except KeyError:
                if "to" in transaction:
                    print(f"{mask_account_card(transaction['to'])}")
                    print(
                        f"Сумма: {transaction['operationAmount']['amount']} "
                        f"{transaction['operationAmount']['currency']['name']}"
                    )
        else:
            try:
                print(f"{get_date(transaction['date'])} {transaction['description']}")
                print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
                print(f"Сумма: {transaction.get('amount')} {transaction.get('currency_code', {})}")
            except ValueError:
                if "to" in transaction:
                    print(f"{mask_account_card(transaction['to'])}")
                    print(f"Сумма: {transaction.get('amount')} {transaction.get('currency_code', {})}")

    if not transactions_data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
