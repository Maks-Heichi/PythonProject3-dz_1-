import json
import logging
import os
from typing import Any, Dict, List


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


logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def log_execution(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} executed successfully.")
            return result
        except Exception as e:
            logger.error(f"Function {func.__name__} failed with error: {e}")
            raise

    return wrapper


@log_execution
def successful_function():
    return "Success!"


@log_execution
def error_function():
    raise ValueError("An error occurred!")


successful_function()

try:
    error_function()
except Exception:
    pass
