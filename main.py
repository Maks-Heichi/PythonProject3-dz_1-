import re
from collections import Counter
from typing import Any, Dict, List

from src.finance_operations_csv import read_transactions_from_csv
from src.finance_operations_exl import read_transactions_from_excel
from src.masks import get_mask_account, get_mask_card_number
from src.utils import load_transactions

ALLOWED_STATUSES = ("EXECUTED", "CANCELED", "PENDING")


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Ищет операции, в описании которых встречается указанная строка."""
    if not search:
        return []

    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [operation for operation in data if pattern.search(str(operation.get("description", "")))]


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций по заданным категориям"""
    if not categories:
        return {}

    compiled = {
        category: re.compile(re.escape(category), re.IGNORECASE) for category in categories
    }

    counter: Counter[str] = Counter()
    for operation in data:
        description = str(operation.get("description", ""))
        for category, pattern in compiled.items():
            if pattern.search(description):
                counter[category] += 1

    return {category: counter.get(category, 0) for category in categories}


def ask_menu_choice() -> int:
    """Запрашивает у пользователя выбор пункта меню (1–3)."""
    while True:
        choice = input().strip()
        if choice in {"1", "2", "3"}:
            return int(choice)
        print("Пожалуйста, введите 1, 2 или 3.")


def ask_status() -> str:
    """Запрашивает статус операции до тех пор, пока не будет введён корректный."""
    while True:
        status = input().strip().upper()
        if status in ALLOWED_STATUSES:
            print(f'Операции отфильтрованы по статусу "{status}"')
            return status
        print(f'Статус операции "{status}" недоступен.')
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )


def ask_yes_no(prompt: str) -> bool:
    """Задаёт пользователю вопрос с ответом Да/Нет."""
    while True:
        answer = input(f"{prompt} ").strip().lower()
        if answer in {"да", "yes", "y"}:
            return True
        if answer in {"нет", "no", "n"}:
            return False
        print('Пожалуйста, ответьте "Да" или "Нет".')


def ask_sort_order() -> bool:
    """Запрашивает порядок сортировки."""
    while True:
        answer = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        if "возраст" in answer:
            return True
        if "убыв" in answer:
            return False
        print('Пожалуйста, введите "по возрастанию" или "по убыванию".')


def filter_by_status(transactions: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """Фильтрует список транзакций по статусу ``state`` (без учёта регистра)."""
    normalized = status.upper()
    return [operation for operation in transactions if str(operation.get("state", "")).upper() == normalized]


def sort_by_date(transactions: List[Dict[str, Any]], ascending: bool) -> List[Dict[str, Any]]:
    """Сортирует операции по полю ``date`` ожидается строка в формате ``YYYY-MM-DDTHH:MM:SS``."""
    return sorted(transactions, key=lambda operation: str(operation.get("date", "")), reverse=not ascending)


def _is_ruble_transaction(transaction: Dict[str, Any]) -> bool:
    """Проверяет, является ли операция рублёвой."""
    currency_code: str = ""

    op_amount = transaction.get("operationAmount")
    if isinstance(op_amount, dict):
        currency = op_amount.get("currency")
        if isinstance(currency, dict):
            currency_code = str(currency.get("code") or currency.get("name") or "")
    else:
        currency_code = str(
            transaction.get("currency_code")
            or transaction.get("currency")
            or transaction.get("currency_name")
            or ""
        )

    code_upper = currency_code.upper()
    return code_upper in {"RUB", "RUR", "РУБ", "РУБ."} or "RUBLE" in code_upper


def filter_ruble_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Возвращает только рублёвые операции."""
    return [operation for operation in transactions if _is_ruble_transaction(operation)]


def format_date(date_string: str) -> str:
    """Преобразует дату формата ``YYYY-MM-DDTHH:MM:SS``в формат ``ДД.ММ.ГГГГ``."""
    if not date_string:
        return ""
    try:
        date_part = date_string.split("T", maxsplit=1)[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except ValueError:
        return date_string


def mask_party(info: str) -> str:
    """Маскирует номер карты или счёта."""
    if not info:
        return ""

    parts = info.split()
    if len(parts) < 2:
        return info

    label = " ".join(parts[:-1])
    number = parts[-1]

    try:
        if "Счет" in label:
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)
    except ValueError:
        return info

    return f"{label} {masked_number}"


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Печатает в консоль список транзакций."""
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши")
        print("условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

    for operation in transactions:
        date_str = format_date(str(operation.get("date", "")))
        description = str(operation.get("description", ""))
        print(f"{date_str} {description}")

        from_value = str(operation.get("from") or "")
        to_value = str(operation.get("to") or "")

        if from_value or to_value:
            if from_value and to_value:
                print(f"{mask_party(from_value)} -> {mask_party(to_value)}")
            elif from_value:
                print(mask_party(from_value))
            else:
                print(mask_party(to_value))

        amount_str: str
        currency_str: str

        op_amount = operation.get("operationAmount")
        if isinstance(op_amount, dict):
            amount_str = str(op_amount.get("amount", ""))

            currency = op_amount.get("currency")
            if isinstance(currency, dict):
                currency_str = str(currency.get("name") or currency.get("code") or "")
            else:
                currency_str = ""
        else:
            amount_str = str(operation.get("amount", ""))
            currency_str = str(
                operation.get("currency_name") or operation.get("currency_code") or operation.get("currency") or ""
            )

        if amount_str or currency_str:
            print(f"Сумма: {amount_str} {currency_str}")

        print()


def main() -> None:
    """
    Основная функция программы. Организует диалог с пользователем: выбор источника данных, фильтрацию по
    статусу, сортировку, фильтрацию по валюте и слову в описании, а также
    вывод итогового списка транзакций.
    """
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    choice = ask_menu_choice()

    if choice == 1:
        print("Для обработки выбран JSON-файл.")
        transactions = load_transactions("data/operations.json")
    elif choice == 2:
        print("Для обработки выбран CSV-файл.")
        transactions = read_transactions_from_csv("transactions.csv", delimiter=";")
    else:
        print("Для обработки выбран XLSX-файл.")
        transactions = read_transactions_from_excel("transactions_excel.xlsx")

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    status = ask_status()
    filtered = filter_by_status(transactions, status)

    if ask_yes_no("Отсортировать операции по дате? Да/Нет"):
        ascending = ask_sort_order()
        filtered = sort_by_date(filtered, ascending)

    if ask_yes_no("Выводить только рублевые транзакции? Да/Нет"):
        filtered = filter_ruble_transactions(filtered)

    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании? Да/Нет"):
        search = input("Введите строку для поиска по описанию: ").strip()
        if search:
            filtered = process_bank_search(filtered, search)

    print("Распечатываю итоговый список транзакций...")
    print_transactions(filtered)


if __name__ == "__main__":
    main()
