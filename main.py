from src.masks import get_mask_account, get_mask_card_number

number_card_user = input("Введите номер карты: ")
print(get_mask_card_number(number_card_user))

number_account_user = input("Введите номер счета: ")
print(get_mask_account(number_account_user))
