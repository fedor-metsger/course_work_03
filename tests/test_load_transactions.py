
import pytest
from utils import load_transactions

TEST_TRANSACTIONS_FILE = "test_transactions.json"


def test_load_transactions():
    print(load_transactions(TEST_TRANSACTIONS_FILE))
    assert load_transactions(TEST_TRANSACTIONS_FILE) == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58',
         'operationAmount': {'amount': '3', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод', 'from': 'Maestro 1234567890123456', 'to': 'Счет 66666666666666666666'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29',
         'operationAmount': {'amount': '4', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод', 'from': 'MasterCard 1234567890123457', 'to': 'Счет 777777777777777777777'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58',
         'operationAmount': {'amount': '9', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод', 'from': 'Счет 99999999999999999999', 'to': 'Счет 88888888888888888888'}]

def test_load_transactions_bad_file():
    assert load_transactions("qwe") == None