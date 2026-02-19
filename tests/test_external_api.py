import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub

class TestConvertToRub(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_convert_to_rub(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "rates": {
                "RUB": 75.0
            }
        }
        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_invalid_currency(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"error": "Invalid currency"}
        with self.assertRaises(Exception):
            convert_to_rub({"amount": 100, "currency": "EUR"})

if __name__ == '__main__':
    unittest.main()