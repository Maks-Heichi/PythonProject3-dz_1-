import unittest
from unittest.mock import mock_open, patch

from src.finance_operations_csv import read_transactions_from_csv


# Тестирование функции
class TestReadTransactionsFromCsv(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="id,amount,date\n1,100,2023-01-01\n2,200,2023-01-02")
    def test_read_transactions(self, mock_file):
        result = read_transactions_from_csv("dummy_path.csv")

        expected = [
            {"id": "1", "amount": "100", "date": "2023-01-01"},
            {"id": "2", "amount": "200", "date": "2023-01-02"},
        ]

        self.assertEqual(result, expected)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
