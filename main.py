from database.database import (
    initialize_database,
    get_balance,
    update_balance,
    record_transaction,
    get_transactions
)


# The resources that exist in Lords Mobile.
# The actual balances are stored in the database.
bank = {
    "food": 0,
    "wood": 0,
    "stone": 0,
    "ore": 0,
    "gold": 0
}


# Make sure the database exists before the bank starts.
initialize_database()


def show_balance():
    """Display the current bank balance."""

    print()
    print("Current Balance")
    print("----------------------")

    print("Food:", get_balance("food"))
    print("Wood:", get_balance("wood"))
    print("Stone:", get_balance("stone"))
    print("Ore:", get_balance("ore"))
    print("Gold:", get_balance("gold"))


def deposit(resource, amount):
    """Add resources to the bank."""

    if resource not in bank:
        print("ERROR: Invalid resource.")
        return

    if amount <= 0:
        print("ERROR: Amount must be greater than 0.")
        return

    update_balance(resource, amount)

    record_transaction(
        "DEPOSIT",
        resource,
        amount
    )

    print("Deposit successful!")


def withdraw(resource, amount):
    """Remove resources from the bank."""

    if resource not in bank:
        print("ERROR: Invalid resource.")
        return

    if amount <= 0:
        print("ERROR: Amount must be greater than 0.")
        return

    current_balance = get_balance(resource)

    if amount > current_balance:
        print("ERROR: Not enough resources in the bank.")
        return

    update_balance(resource, -amount)

    record_transaction(
        "WITHDRAWAL",
        resource,
        -amount
    )

    print("Withdrawal successful!")


def show_transactions():
    """Display the bank's transaction history."""

    transactions = get_transactions()

    print()
    print("Transaction History")
    print("----------------------")

    if not transactions:
        print("No transactions yet.")
        return

    for transaction in transactions:

        transaction_id, timestamp, transaction_type, resource, amount = transaction

        print(
            transaction_id,
            "|",
            timestamp,
            "|",
            transaction_type,
            "|",
            resource,
            "|",
            amount
        )


while True:

    print()
    print("LordsBot Personal Bank")
    print("----------------------")
    print("1. Check balance")
    print("2. Deposit resources")
    print("3. Withdraw resources")
    print("4. Transaction history")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        show_balance()

    elif choice == "2":

        resource = input(
            "Enter resource (food, wood, stone, ore, gold): "
        ).lower()

        amount = int(
            input("Enter amount: ")
        )

        deposit(resource, amount)

    elif choice == "3":

        resource = input(
            "Enter resource (food, wood, stone, ore, gold): "
        ).lower()

        amount = int(
            input("Enter amount: ")
        )

        withdraw(resource, amount)

    elif choice == "4":

        show_transactions()

    elif choice == "5":

        print("LordsBot shutting down.")
        break

    else:

        print("ERROR: Invalid option.")