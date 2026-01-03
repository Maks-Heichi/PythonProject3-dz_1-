def mask_card(card_number: str) -> str:
    """Маскируем номер карты, оставляя последние 4 цифры и 4 цифры в начале"""
    return card_number[:4] + ' ' + ' '.join(['**' for _ in range((len(card_number) - 8) // 4)]) + ' ' + card_number[-4:]

def mask_account(account_number: str) -> str:
    """Маскируем номер счета, оставляя последние 4 цифры"""
    return '**' + account_number[-4:]

def mask_account_card(info: str) -> str:
    """Обрабатывает информацию о картах и счетах, возвращая замаскированный номер"""
    parts = info.split()
    card_type = ' '.join(parts[:-1])
    number = parts[-1]

    if 'Счет' in card_type:
        masked_number = mask_account(number)
    else:
        masked_number = mask_card(number)

    return f"{card_type} {masked_number}"

def get_date(date_string: str) -> str:
    """Форматирует дату из строки формата 'YYYY-MM-DD T HH:MM:SS' в формат 'ДД.ММ.ГГГГ'"""
    date_part = date_string.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"

# Примеры работы функций
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))