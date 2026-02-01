from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize('x', 'y' [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305','Счет **4305')
])


def test_mask_account_card(x, y):
    assert mask_account_card(x) == y


def test_get_date():
    assert get_date('2026-01-04T013:00:00.671407') == '04.01.2026'