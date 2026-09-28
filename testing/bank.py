def deposit(balance, amount):
    if amount <= 0:
        return balance

    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        return balance

    if amount > balance:
        return balance

    return balance - amount