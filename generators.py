def filter_by_currency(transactions: List[Dict[str, Optional[str]]], currency: str):
    """Генератор, фильтрующий транзакции по указанной валюте"""
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Optional[str]]]):
    """Генератор, выдающий описания транзакций по очереди"""
    for transaction in transactions:
        yield transaction.get('description', 'Описание отсутствует')


#Пример входных данных для проверки функций "filter_by_currency" и "transaction_descriptions"
if __name__ == "__main__":
    transactions_list = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


    #Пример использования функции filter_by_currency
    usd_transactions = filter_by_currency(transactions, "USD")
    for i in range(2):
        print(next(usd_transactions))


    #Пример использования функции transaction_descriptions
    descriptions = transaction_descriptions(transactions)
    for i in range(5):
        print(next(descriptions))


def card_number_generator(start: Any, end: Any) -> List[Dict[str, str]]:
    """Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        card = f"{number:016}"
        formatted_number = f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
        yield formatted_number

# Пример использования:
for card_number in card_number_generator(1, 5):
    print(card_number)