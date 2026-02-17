import unittest
from unittest.mock import patch, MagicMock
import json
from src.utils import load_transactions


@patch('builtins.open', new_callable=MagicMock)
def test_load_transactions(self, mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = json.dumps([{"amount": 100, "currency": "USD"}])
    result = load_transactions('data/operations.json')
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0]['amount'], 100)
