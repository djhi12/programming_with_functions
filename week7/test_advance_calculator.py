import pytest
import advance_calculator  # Assuming your main program file is named 'calculator.py'

# Test addition function
def test_addition():
    assert advance_calculator.add(3, 5) == 8
    assert advance_calculator.add(-2, 2) == 0
    assert advance_calculator.add(0, 0) == 0

# Test subtraction function
def test_subtraction():
    assert advance_calculator.subtract(5, 3) == 2
    assert advance_calculator.subtract(2, 2) == 0
    assert advance_calculator.subtract(0, 5) == -5

# Test multiplication function
def test_multiplication():
    assert advance_calculator.multiply(3, 5) == 15
    assert advance_calculator.multiply(-2, 2) == -4
    assert advance_calculator.multiply(0, 5) == 0

# Test division function
def test_division():
    assert advance_calculator.divide(10, 2) == 5
    assert advance_calculator.divide(5, 0) == "Cannot divide by zero."

# Test exponentiation function
def test_exponentiation():
    assert advance_calculator.exponentiate(2, 3) == 8
    assert advance_calculator.exponentiate(3, 2) == 9
    assert advance_calculator.exponentiate(5, 0) == 1

# Test square root function
def test_square_root():
    assert advance_calculator.square_root(25) == 5
    assert advance_calculator.square_root(16) == 4
    assert advance_calculator.square_root(-4) == "Invalid input. Cannot calculate the square root of a negative number."

# Test trigonometric functions
def test_trigonometric_functions():
    assert advance_calculator.trigonometric_functions(1, 30) == 0.5
    assert advance_calculator.trigonometric_functions(2, 45) == 0.7071067811865476
    assert advance_calculator.trigonometric_functions(3, 60) == 1.7320508075688772

# Add more test cases as needed

