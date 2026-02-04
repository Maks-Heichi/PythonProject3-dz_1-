from generators.py import filter_by_currency, transaction_descriptions, card_number_generator
import pytest

def test_filter_by_currency(transactions):
    result = filter_by_currency(transactions, "USD")
    assert len(result) == 3


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert len(descriptions) == len(transactions)


def test_card_number_generator():
    card_numbers = card_number_generator(transactions)
    assert len(card_numbers) == 5