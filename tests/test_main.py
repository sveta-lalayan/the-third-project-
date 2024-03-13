import json
import datetime

import ROOT_DIR from config



def test_load_transactions():
    with open('operations.json', 'r') as file:
        transactions = json.load(file)
    assert load_transactions() == transactions

def test_display_executed_transactions():
    transactions = [
        {
            "date": "2022-01-01T12:00:00.000Z",
            "description": "Test Description 1",
            "state": "EXECUTED",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD"}},
            "to": "Счет 1234567890123456",
        },
        {
            "date": "2022-01-02T12:00:00.000Z",
            "description": "Test Description 2",
            "state": "CANCELED",
            "operationAmount": {"amount": "200.00", "currency": {"name": "USD"}},
            "to": "Счет 2222222222222222",
        },
    ]
    executed_transactions = display_executed_transactions(transactions)
    assert len(executed_transactions) == 1

def test_show_five_transactions():
    transactions = [
        {
            "date": "2022-01-01T12:00:00.000Z",
            "description": "Test Description 1",
            "state": "EXECUTED",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD"}},
            "to": "Счет 1234567890123456",
        },
        {
            "date": "2022-01-02T12:00:00.000Z",
            "description": "Test Description 2",
            "state": "EXECUTED",
            "operationAmount": {"amount": "200.00", "currency": {"name": "USD"}},
            "to": "Счет 2222222222222222",
        },
    ]
    executed_transactions = display_executed_transactions(transactions)
    five_transactions = show_five_transactions(executed_transactions)
    assert len(five_transactions) == 1

def test_mask_star_number():
    assert mask_star_number("Счет 1234567890123456") == "Счет **1234"
    assert mask_star_number("1234 5678 1234 5678") == "1234 5678 **** 5678"

def test_transaction_format():
    date = "2022-01-01T12:00:00.000Z"
    description = "Test Description"
    amount = "100.00"
    currency = "USD"
    to = "Счет 1234567890123456"
    from_ = "Счет 1111111111111111"
    expected = "01.01.2022 Test Description\nСчет 1111 5678 **** 5678 -> Счет **1234\n100.00 USD"
    assert transaction_format(date, description, amount, currency)

