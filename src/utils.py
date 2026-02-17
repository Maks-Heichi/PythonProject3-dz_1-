import json
import os
from typing import List, Dict, Any


def load_transactions(operations: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(operations.json) as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # Если файл не найден или данные не являются корректным JSON, возвращаем пустой список

    return [] # На случай, если данные не являются списком