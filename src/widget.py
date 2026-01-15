from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """Обрабатывает информацию о картах и счетах, возвращая замаскированный номер"""
    parts = info.split()
    card_type = ' '.join(parts[:-1])
    number = parts[-1]

    if 'Счет' in card_type:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"

def get_date(date_string: str) -> str:
    """Форматирует дату из строки формата 'YYYY-MM-DD T HH:MM:SS' в формат 'ДД.ММ.ГГГГ'"""
    date_part = date_string.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"

# Примеры работы функций
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2026-01-04T013:00:00.671407"))