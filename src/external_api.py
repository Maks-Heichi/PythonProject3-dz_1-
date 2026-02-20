import json
import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """Конвертирует сумму в другую валюту в рубли."""
    if currency == "RUB":
        return amount  # Если валюта уже в рублях, просто возвращаем сумму

    url = f"https://api.apilayer.com/exchangerates_data/convert?base={currency}&symbols=RUB"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    # Проверяем успешность запроса
    if response.status_code != 200:
        print(f"Код статуса ответа: {response.status_code}")
        print(f"Содержимое ответа: {response.text}")
        raise Exception("Ошибка при получении курсов валют")

    # Извлекаем курс рубля из ответа
    rate = response.json()["rates"]["RUB"]
    return amount * rate  # Возвращаем конвертированную сумму


# Примеры транзакций
try:
    # Конвертация и вывод результата для USD
    amount_in_rub_usd = convert_to_rub(transaction_usd)
    print(f"Транзакция в размере 100 USD составляет: {amount_in_rub_usd:.2f} рублей")

    # Конвертация и вывод результата для EUR
    amount_in_rub_eur = convert_to_rub(transaction_eur)
    print(f"Транзакция в размере 100 EUR составляет: {amount_in_rub_eur:.2f} рублей")
except Exception as e:
    print(f"Error: {e}")  # Обработка ошибок
