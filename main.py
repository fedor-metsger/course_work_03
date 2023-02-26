
from utils import load_transactions

JSON_URL = "https://www.jsonkeeper.com/b/ZJZP"
TRANSACTIONS_FILE = "operations.json"

def main():
    """
    main
    """
    trans = load_transactions(TRANSACTIONS)
    print(trans)

if __name__ == "__main__":
    main()