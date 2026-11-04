from app import add_numbers, subtract_numbers
def test_addition():
    assert add_numbers(10, 20) == 30
def test_subtraction():
    assert subtract_numbers(20, 10) == 10
def test_addition_with_negative_numbers():
    assert add_numbers(-5, 10) == 5
