
from utils import load_transactions, get_filtered, get_first, get_formatted

JSON_URL = "https://www.jsonkeeper.com/b/ZJZP"
TRANSACTIONS_FILE = "operations.json"
COUNT_TO_PRINT = 5


def print_stats(trans):
    """
    Выводит на консоль статистику по загруженным данным
    Используется для отладки
    """
    cnt, cnt_from, cnt_to, states, tr_from, tr_to = 0, 0, 0, set(), set(), set()
    for tr in trans:
        if "state" in tr:
            states = states | {tr["state"]}
            cnt += 1
        if "from" in tr:
            tr_from = tr_from | {' '.join(tr["from"].split()[:-1])}
            cnt_from += 1
        if "to" in tr:
            tr_to = tr_to | {' '.join(tr["to"].split()[:-1])}
            cnt_to += 1

    print(f"Атрибут 'state' есть у {cnt} транзакций")
    print(str(states))
    print(f"Атрибут 'from' есть у {cnt_from} транзакций")
    print(tr_from)
    print(f"Атрибут 'to' есть у {cnt_to} транзакций")
    print(tr_to)


def main():
    """
    main
    """
    trans = load_transactions(TRANSACTIONS_FILE)
#    trans = load_transactions("test_transactions.json")
    if not trans:
        return
#    print(f"Загружено {len(trans)} транзакций")
#    print_stats(trans)

    trans = get_filtered(trans)
#    print(f"Отфильтровано {len(trans)} транзакций по статусу {FILTER_STATE}")

    trans = get_first(trans, COUNT_TO_PRINT)

    first = True
    for tr in trans:
        if first:
           first = False
        else:
            print()
        print(get_formatted(tr))


if __name__ == "__main__":
    main()
