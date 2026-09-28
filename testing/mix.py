def divide(a, b):
    return a / b

class AgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise AgeError("You must be 18 or older")

    return True


def is_passing(marks):
    return marks >= 40


class InsufficientBalanceError(Exception):
    pass


def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    return balance - amount

