import pytest

@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

@pytest.mark.parametrize("number", [1, 2, 3])
def test_even_number(numbers, number):
    assert number % 2 == 0

def test_sum(numbers):
    assert sum(numbers) == 15
    
