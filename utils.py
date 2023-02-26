
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

def get_filtered(transactions, state):
    """
    Получает на вход список транзакций
    Возвращает список транзакций, отфильтрованный по
    полю state'
    """
    res = []
    for i in transactions:
        try:
            if i["state"] == state:
                res.append(i)
        except Exception as e:
            pass
#            print( "get_filtered:ERROR:", repr(e))
    return res


def get_date(transaction):
    """
    Получает словарь с данными по транзакции и возвращает строку с дотой
    """
    return transaction["date"]


def get_first(transactions, cnt):
    """
    Сортирует список транзакций по полю "date"
    Возвращает нужное количество записей от начала списка
    """
    transactions.sort(key = get_date, reverse = True)
    return transactions[:cnt]


def format_from_to(in_str):
    if in_str[0:4] == "Счет": return "Счет **" + in_str[-4:]
    else:
        name, num = ' '.join(in_str.split()[:-1]), in_str.split()[-1]
        num = f"{num[0:4]} {num[4:6]}** **** {num[12:16]}"
        return f"{name} {num}"


def get_formatted(transaction):
    """
    Получет на вход данные одной транзакции
    Возвращает их в нужном формате
    """
    date = '.'.join([transaction["date"][5:7], transaction["date"][8:10], transaction["date"][0:4]])
    descr = transaction["description"]
    tr_from = "[Нет данных]"
    try:
        tr_from = format_from_to(transaction["from"])
    except:
        pass
#    if tr_from[0:4] == "Счет": tr_from = "Счет **" + tr_from[-4:]
    tr_to = "[Нет данных]"
    try:
        tr_to = format_from_to(transaction["to"])
    except:
        pass
    amount = transaction["operationAmount"]["amount"]
    curr = transaction["operationAmount"]["currency"]["name"]

    return f"{date} {descr}\n{tr_from} -> {tr_to}\n{amount} {curr}"
