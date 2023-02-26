
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
#            print("INFO: Данные загружены успешно")
            return tr_list
    except Exception as e:
        print("ERROR: Ошибка при загрузке транзакций из файла:", repr(e))
        return None


def get_filtered(transactions, state):
    """
    Получает на вход список транзакций
    Возвращает список транзакций, отфильтрованный по
    полю state'
    """
    res = []
    for i in transactions:
        if "state" in i and i["state"] == state:
            res.append(i)
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
    transactions.sort(key=get_date, reverse=True)
    return transactions[:cnt]


def format_from_to(in_str):
    if in_str.split()[0] == "Счет":
        return "Счет **" + in_str[-4:]
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
    descr, tr_from, tr_to = "[Описание отсутствует]", "[Нет данных]", "[Нет данных]"
    if "description" in transaction:
        descr = transaction["description"]
    if "from" in transaction:
        tr_from = format_from_to(transaction["from"])
    if "to" in transaction:
        tr_to = format_from_to(transaction["to"])

    amount = transaction["operationAmount"]["amount"]
    curr = transaction["operationAmount"]["currency"]["name"]

    return f"{date} {descr}\n{tr_from} -> {tr_to}\n{amount} {curr}"
