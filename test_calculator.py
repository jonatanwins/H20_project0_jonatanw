import calculator
import math

def test_add_integers_excercice_1():
    assert calculator.add(1,2) == 3

def test_add_float_excercice_2():
    assert round(calculator.add(0.1,0.2),1) == 0.3

def test_add_string_excercice_3():
    assert calculator.add('IN','1910') == 'IN1910'

def test_factorial_excercice_4():
    assert calculator.factorial(5) == math.factorial(5)

def test_sin_excercice_4():
    assert calculator.sin(0,0) == 0

def test_divide_excercice_4():
    assert calculator.divide(6,3) == 2

def test_double_factorial_excercice_4():
    assert calculator.double_factorial(8) == 384

def test_absolute_value_excercice_4():
    assert calculator.absolute_value(-5) == calculator.absolute_value(5)