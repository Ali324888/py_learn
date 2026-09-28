import pytest
from mix import divide, AgeError, check_age, is_passing, InsufficientBalanceError, deposit, withdraw


def test_divide():
    assert divide(6,2) == 3


def test_divide_decimal():
    assert divide(20,5) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)


def test_valid_age():
   assert check_age(20) == True


def test_invalid_age():
    with pytest.raises(AgeError, match="You must be 18 or older"):
        check_age(15)

def test_passing():
    assert is_passing(50) == True
    assert is_passing(100) == True

def test_failing():
    assert is_passing(30) == False
    assert is_passing(0) == False

def test_exact_boundry():
    assert is_passing(40) == True



def test_deposit():
    assert deposit(1000,500) == 1500

def test_invalid_amount():
    with pytest.raises(ValueError):
        deposit(1000, 0)
        deposit(1000, -100)
        withdraw(1000, 0)

def test_insufficient_balance():
    with pytest.raises(InsufficientBalanceError):
        withdraw(1000, 1500)