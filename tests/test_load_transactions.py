
import pytest
from utils import load_transactions, get_filtered, get_date, get_first, get_formatted, format_from_to

TEST_TRANSACTIONS_FILE = "test_transactions.json"


def test_load_transactions():
    print(load_transactions(TEST_TRANSACTIONS_FILE))
    assert load_transactions(TEST_TRANSACTIONS_FILE) == [
        {'id': 3, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.555555',
         'operationAmount': {'amount': '9', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод', 'from': 'Счет 99999999999999999999', 'to': 'Счет 88888888888888888888'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.555555',
         'operationAmount': {'amount': '3', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод', 'from': 'Maestro 1234567890123456', 'to': 'Счет 66666666666666666666'},
        {'id': 2, 'state': 'NOT_EXECUTED', 'date': '2019-07-03T18:35:29.555555',
         'operationAmount': {'amount': '4', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод', 'from': 'MasterCard 1234567890123457', 'to': 'Счет 777777777777777777777'}]

def test_load_transactions_bad_file():
    assert load_transactions("qwe") == None


def test_get_filtered():
    assert len(get_filtered(load_transactions(TEST_TRANSACTIONS_FILE), "EXECUTED")) == 2
    assert len(get_filtered(load_transactions(TEST_TRANSACTIONS_FILE), "NOT_EXECUTED")) == 1
    assert len(get_filtered(load_transactions(TEST_TRANSACTIONS_FILE), "qwe")) == 0

def test_get_date():
    assert get_date(load_transactions(TEST_TRANSACTIONS_FILE)[0]) == "2018-06-30T02:08:58.555555"


def test_get_first():
    assert get_first(load_transactions(TEST_TRANSACTIONS_FILE), 2) == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.555555',
         'operationAmount': {'amount': '3', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод', 'from': 'Maestro 1234567890123456', 'to': 'Счет 66666666666666666666'},
        {'id': 2, 'state': 'NOT_EXECUTED', 'date': '2019-07-03T18:35:29.555555',
         'operationAmount': {'amount': '4', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод', 'from': 'MasterCard 1234567890123457', 'to': 'Счет 777777777777777777777'}]


def test_get_formatted():
    assert get_formatted(load_transactions(TEST_TRANSACTIONS_FILE)[0]) == \
        "06.30.2018 Перевод\nСчет **9999 -> Счет **8888\n9 USD"


def test_format_from_to():
    assert format_from_to("Счет 99999999999999999999") == "Счет **9999"
    assert format_from_to("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert format_from_to("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert format_from_to("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert format_from_to("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"