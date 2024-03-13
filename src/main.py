import json
from datetime import datetime


# Функция загружает транзакции из json документа
def load_transactions():
    with open('operations.json', 'r') as file:
        transactions = json.load(file)
    return transactions

# Функция показывает выполненные транзакций
def display_executed_transactions(transactions):
    executed_transactions = [transaction for transaction in transactions if transaction and 'executed' in transaction['state'].lower()]
    return executed_transactions



# Функция показывает 5 последних транзакций
def show_five_transactions(executed_transactions):
    sorted_transactions = sorted(executed_transactions, key=lambda x: datetime.fromisoformat(x["date"]), reverse=True)
    return sorted_transactions[:5]


# Функция скрывает номера

def mask_star_number(card_number):
    if card_number.startswith('Счет'):
        return f'Счет **{card_number[-4:]}'
    else:
        id, digits = card_number.rsplit(" ", 1)
        return f'{id} {digits[:4]} {digits[4:6]}** **** {digits[-4:]}'

def transaction_format(date, description, amount, currency, to, from_=None):
    if from_:
        value_from = mask_star_number(from_)
    value_to = mask_star_number(to)
    if from_:
        operation = f'{value_from} -> {value_to}'
    else:
        operation = value_to
    return (f'{datetime.fromisoformat(date).strftime("%d.%m.%Y")} {description}\n'
        f'{operation}\n{amount} {currency}')


# Функция выводит информакцию
def show_transactions(filtered_json):
    for transaction in filtered_json:
        print(transaction_format(
            transaction['date'],
            transaction['description'],
            transaction['operationAmount']['amount'],
            transaction['operationAmount']['currency']['name'],
            transaction['to'],
            transaction.get('from')
        ))
        print()

show_transactions(show_five_transactions(display_executed_transactions(load_transactions())))

