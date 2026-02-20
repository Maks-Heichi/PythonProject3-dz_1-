import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(operations: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(
            operations,
            "r",
            encoding="UTF-8",
        ) as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Если файл не найден или данные не являются корректным JSON, возвращаем пустой список

    return []  # На случай, если данные не являются списком
