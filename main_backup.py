bank = {
    "food": 0,
    "wood": 0,
    "stone": 0,
    "ore": 0,
    "gold": 0
}


def deposit(resource, amount):

    if resource not in bank:
        print("ERROR: Invalid resource.")
        return

    if amount <= 0:
        print("ERROR: Amount must be greater than 0.")
        return

    bank[resource] = bank[resource] + amount

    print("Deposit successful!")


def withdraw(resource, amount):

    if resource not in bank:
        print("ERROR: Invalid resource.")
        return

    if amount <= 0:
        print("ERROR: Amount must be greater than 0.")
        return

    if amount > bank[resource]:
        print("ERROR: Not enough resources in the bank.")
        return

    bank[resource] = bank[resource] - amount

    print("Withdrawal successful!")


print("LordsBot Personal Bank")
print("----------------------")

print("Food:", bank["food"])
print("Wood:", bank["wood"])
print("Stone:", bank["stone"])
print("Ore:", bank["ore"])
print("Gold:", bank["gold"])


print()
print("Depositing 10,000,000 food...")

deposit("food", 10000000)


print()
print("Current balance:")

print("Food:", bank["food"])
print("Wood:", bank["wood"])
print("Stone:", bank["stone"])
print("Ore:", bank["ore"])
print("Gold:", bank["gold"])


print()
print("Withdrawing 3,000,000 food...")

withdraw("food", 3000000)


print()
print("Final balance:")

print("Food:", bank["food"])
print("Wood:", bank["wood"])
print("Stone:", bank["stone"])
print("Ore:", bank["ore"])
print("Gold:", bank["gold"])
print()
print("Testing withdrawal larger than balance...")

withdraw("food", 10000000)
print()
print("Testing invalid withdrawal...")

withdraw("banana", 5000000)
withdraw("food", -5000000)