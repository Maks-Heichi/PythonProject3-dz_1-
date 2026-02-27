import pandas as pd


def read_transactions_from_excel(file_path: str):
    """Чтение Excel-файла с помощью pandas"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    # Пример использования функции
    transactions = read_transactions_from_excel("transactions_excel.xlsx")
    for transaction in transactions:
        print(transaction)
