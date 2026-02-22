import json
import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """Конвертирует сумму в другую валюту в рубли."""
    if currency == "RUB":
        return amount  # Если валюта уже в рублях, просто возвращаем сумму

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Ошибка при получении курсов валют")

    converted_amount = response.json()["result"]
    return converted_amount  # Возвращаем конвертированную сумму


def load_transactions(file_path: str):
    """Загружает транзакции из JSON-файла."""
    with open(file_path, "r", encoding="UTF-8") as file:
        return json.load(file)


def process_transaction(transaction):
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    return convert_to_rub(amount, currency)


if __name__ == "__main__":
    try:
        transactions = load_transactions("operations.json")

        for transaction in transactions:
            amount_in_rub = process_transaction(transaction)
            print(
                f"Транзакция в размере {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['code']} составляет: {amount_in_rub:.2f} рублей"
            )

    except Exception as e:
        print(f"Error: {e}")  # Обработка ошибок
