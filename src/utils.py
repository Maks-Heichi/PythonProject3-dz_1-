import json
import logging
import os
from typing import List, Dict, Any


def load_transactions(operations: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(operations, 'r', encoding="UTF-8",) as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # Если файл не найден или данные не являются корректным JSON, возвращаем пустой список

    return [] # На случай, если данные не являются списком


logger = logging.getLogger(__name__)
# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler('logs/utils.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


logger = logging.getLogger(__name__)
logging.basicConfig(filename='utils.log', filemode='w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
