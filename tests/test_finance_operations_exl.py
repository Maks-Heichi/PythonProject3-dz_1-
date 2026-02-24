import unittest
from unittest.mock import patch

import pandas as pd

from src.finance_operations_exl import read_transactions_from_excel


# Тестирование функции
class TestReadTransactionsFromExcel(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_transactions(self, mock_read_excel):
        # Создаем имитацию DataFrame с тестовыми данными
        test_data = {"id": [1, 2], "amount": [100, 200], "date": ["2023-01-01", "2023-01-02"]}
        mock_df = pd.DataFrame(test_data)
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel("dummy_path.xlsx")

        expected = [{"id": 1, "amount": 100, "date": "2023-01-01"}, {"id": 2, "amount": 200, "date": "2023-01-02"}]

        self.assertEqual(result, expected)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
