import csv
from typing import Dict, List


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """Чтение CSV-файла и возврат списка словарей"""
    transactions = []
    with open(file_path, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)  # Добавляем каждую строку в список
    return transactions


# Пример использования функции
csv_transactions = read_transactions_from_csv("transactions.csv")
for transaction in csv_transactions:
    print(transaction)
