from generators.py import filter_by_currency, transaction_descriptions, card_number_generator
import pytest

def test_filter_by_currency(transactions):
    result = filter_by_currency(transactions, "USD")
    assert len(result) == 3
