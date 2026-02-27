import csv
from typing import Dict, List


def read_transactions_from_csv(file_path: str, delimiter: str = ",") -> List[Dict]:
    """Чтение CSV-файла и возврат списка словарей"""
    transactions = []
    with open(file_path, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        for row in reader:
            transactions.append(row)  # Добавляем каждую строку в список
    return transactions


if __name__ == "__main__":
    # Пример использования функции
    csv_transactions = read_transactions_from_csv("transactions.csv", delimiter=";")  # Укажите нужный разделитель
    for transaction in csv_transactions:
        print(transaction)
