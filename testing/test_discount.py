from discount import calculate_discount

def test_discount():
    assert calculate_discount(1000,10) == 900


def test_no_discount():
    assert calculate_discount(1000,0) == 1000