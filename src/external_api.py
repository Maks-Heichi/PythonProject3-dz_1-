import os
import requests
import json
from dotenv import load_dotenv
from typing import Dict

load_dotenv('.env')
API_KEY = os.getenv('API_KEY')


def convert_to_rub(transaction: Dict[str, float]) -> float:
    """Конвертирует сумму в другую валюту в рубли."""
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return amount  # Если валюта уже в рублях, просто возвращаем сумму

    url = f"https://api.apilayer.com/exchangerates_data/convert?base={currency}&symbols=RUB"
    headers = {'apikey': API_KEY}
    response = requests.get(url, headers=headers)

    # Проверяем успешность запроса
    if response.status_code != 200:
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        raise Exception("Error fetching exchange rates")

    # Извлекаем курс рубля из ответа
    rate = response.json()['rates']['RUB']
    return amount * rate  # Возвращаем конвертированную сумму


# Примеры транзакций
transaction_usd = {'amount': 100, 'currency': 'USD'}
transaction_eur = {'amount': 100, 'currency': 'EUR'}

try:
    # Конвертация и вывод результата для USD
    amount_in_rub_usd = convert_to_rub(transaction_usd)
    print(f"Transaction {transaction_usd} is {amount_in_rub_usd:.2f} RUB")

    # Конвертация и вывод результата для EUR
    amount_in_rub_eur = convert_to_rub(transaction_eur)
    print(f"Transaction {transaction_eur} is {amount_in_rub_eur:.2f} RUB")
except Exception as e:
    print(f"Error: {e}")  # Обработка ошибок