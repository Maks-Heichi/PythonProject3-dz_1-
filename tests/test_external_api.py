import unittest
from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub, load_transactions, process_transaction


class TestCurrencyConverter(unittest.TestCase):

    @patch("requests.get")
    @patch("os.getenv")
    def test_convert_to_rub(self, mock_getenv, mock_get):
        mock_getenv.return_value = "dummy_api_key"

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 1000}

        result = convert_to_rub(100, "USD")
        self.assertEqual(result, 1000)

    @patch("requests.get")
    def test_convert_to_rub_error(self, mock_get):
        mock_get.return_value.status_code = 400  # Симуляция ошибки API
        with self.assertRaises(Exception) as context:
            convert_to_rub(100, "USD")
        self.assertIn("Ошибка при получении курсов валют", str(context.exception))


class TestLoadTransactions(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}]',
    )
    def test_load_transactions(self, mock_file):
        transactions = load_transactions("dummy_path.json")
        expected = [{"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}]
        self.assertEqual(transactions, expected)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_transactions_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            load_transactions("dummy_path.json")


class TestProcessTransaction(unittest.TestCase):

    @patch("src.external_api.convert_to_rub")
    def test_process_transaction(self, mock_convert_to_rub):
        mock_convert_to_rub.return_value = 1000
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
        result = process_transaction(transaction)
        self.assertEqual(result, 1000)
        mock_convert_to_rub.assert_called_once_with(100, "USD")


if __name__ == "__main__":
    unittest.main()
