from typing import Any, Dict, Iterator, List, Optional


def filter_by_currency(transactions: List[Dict[str, Optional[str]]], currency: str):
    """Генератор, фильтрующий транзакции по указанной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transaction: Dict[str, Optional[str]]):
    """
    Генератор, выдающий описание одной транзакции.

    По тестам функция получает одну транзакцию (словарь) и должна
    вернуть её описание при первом вызове next(...).
    """
    yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: Any, end: Any) -> Iterator[str]:
    """Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        card = f"{number:016}"
        formatted_number = f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
        yield formatted_number


if __name__ == "__main__":
    # Пример входных данных для проверки функций
    transactions_list = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

    # Пример использования функции filter_by_currency
    usd_transactions = filter_by_currency(transactions_list, "USD")
    print(next(usd_transactions))

    # Пример использования функции transaction_descriptions
    description_gen = transaction_descriptions(transactions_list[0])
    print(next(description_gen))

    # Пример использования генератора номеров карт
    for card_number in card_number_generator(1, 5):
        print(card_number)