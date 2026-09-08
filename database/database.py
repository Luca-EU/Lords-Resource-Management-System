import sqlite3
from datetime import datetime


def initialize_database():
    connection = sqlite3.connect("lordsbot.db")
    cursor = connection.cursor()

    # Create the bank table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bank (
        resource TEXT PRIMARY KEY,
        amount INTEGER
    )
    """)

    # Create the transaction history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        transaction_type TEXT,
        resource TEXT,
        amount INTEGER
    )
    """)

    # Add the five resources if they do not already exist
    resources = [
        ("food", 0),
        ("wood", 0),
        ("stone", 0),
        ("ore", 0),
        ("gold", 0)
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO bank (resource, amount) VALUES (?, ?)",
        resources
    )

    connection.commit()
    connection.close()


def get_balance(resource):
    connection = sqlite3.connect("lordsbot.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT amount FROM bank WHERE resource = ?",
        (resource,)
    )

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return None

    return result[0]


def update_balance(resource, amount):
    connection = sqlite3.connect("lordsbot.db")
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE bank SET amount = amount + ? WHERE resource = ?",
        (amount, resource)
    )

    connection.commit()
    connection.close()


def record_transaction(transaction_type, resource, amount):
    connection = sqlite3.connect("lordsbot.db")
    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO transactions
        (timestamp, transaction_type, resource, amount)
        VALUES (?, ?, ?, ?)
        """,
        (timestamp, transaction_type, resource, amount)
    )

    connection.commit()
    connection.close()


def get_transactions():
    connection = sqlite3.connect("lordsbot.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, timestamp, transaction_type, resource, amount
        FROM transactions
        ORDER BY id DESC
    """)

    transactions = cursor.fetchall()

    connection.close()

    return transactions


def reset_bank():
    connection = sqlite3.connect("lordsbot.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE bank SET amount = 0")
    cursor.execute("DELETE FROM transactions")

    connection.commit()
    connection.close()