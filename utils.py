
import json

def load_transactions(filename: str):
    """
    Загружает список транзакций из файла
    Возвращает список
    """

#    tr_list = requests.get(JSON_URL).json()
    with open(TRANSACTIONS_FILE, mode='r', encoding='utf-8') as inf:
        tr_list = json.load(inf)

    return tr_list