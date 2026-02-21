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
    logger.info("Загружается транзакция")
    try:
        with open(
            operations,
            "r",
            encoding="UTF-8",
        ) as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Транзакция успешно загружена")
                return data

    except FileNotFoundError:
        error_msg = "Файл не найден"
        logger.error(error_msg)
        raise ValueError(error_msg)
    except json.JSONDecodeError:
        error_msg = "Данные не являются корректным"
        logger.error(error_msg)
        raise ValueError(error_msg)

    return []  # На случай, если данные не являются списком
