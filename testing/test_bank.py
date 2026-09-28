from bank import deposit, withdraw

def test_deposit():
    assert deposit(1000,500) == 1500
    assert deposit(1000,0) == 1000
    assert deposit(1000,-100) == 1000

def test_withdraw():
    assert withdraw(1000, 300) == 700
    assert withdraw(1000, 0) == 1000
    assert withdraw(1000, 1500) == 1000