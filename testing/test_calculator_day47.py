from calculator_day47 import add, subtract, multiply, divide



def test_add():
    assert add(10,20) == 30


def test_subtract():
    assert subtract(10,5) == 5


def test_multiply():
    assert multiply(2,10) == 20


def test_divide():
    assert divide(10,2) == 5