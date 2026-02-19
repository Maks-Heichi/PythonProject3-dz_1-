from typing import Any, Dict, Iterator, List, Optional

# Примеры
transactions_list: List[Dict[str, Optional[str]]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# Функция filter_by_state
def filter_by_state(
    transactions: List[Dict[str, Optional[str]]], state: str = "EXECUTED"
) -> List[Dict[str, Optional[str]]]:
    """Фильтрует список транзакций по значению ключа state."""
    return [transaction for transaction in transactions if transaction.get("state") == state]


executed_transactions = filter_by_state(transactions_list)
print(executed_transactions)

canceled_transactions = filter_by_state(transactions_list, "CANCELED")
print(canceled_transactions)


# Функции sort_by_date
def sort_by_date(
    transactions: List[Dict[str, Optional[str]]], descending: bool = True
) -> List[Dict[str, Optional[str]]]:
    """Сортирует список транзакций по дате."""
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)


sorted_transactions = sort_by_date(transactions_list)
print(sorted_transactions)
