
import json

def load_transactions(filename: str):
    """
    Загружает список транзакций из файла
    Возвращает список
    """

#    tr_list = requests.get(JSON_URL).json()
    try:
        with open(filename, mode='r', encoding='utf-8') as inf:
            tr_list = json.load(inf)
        if tr_list:
            print("INFO: Данные загружены успешно")
            return tr_list
    except:
        print("ERROR: Ошибка при загрузке транзакций")
        return None