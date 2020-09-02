import calculator
import math
import pytest

# Excercice 1
def test_add_integers_excercice_1():
    assert calculator.add(1,2) == 3

# Excercice 2
def test_add_float_excercice_2():
    assert math.isclose(calculator.add(0.1,0.2),0.3, rel_tol=0.0001)

# Excercice 3
def test_add_string_excercice_3():
    assert calculator.add('IN','1910') == 'IN1910'

# Excercice 4
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

# Excercice 5
def test_add_excercice_5():
    with pytest.raises(TypeError):
        calculator.add('4',2)

def test_divide_by_zero_excercice_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1,0)

# Excercice 6
@pytest.mark.parametrize("arg, expected_output", [[(-1,1),0],[('ananas','biter'),'ananasbiter']])
def test_add_integer_string_excercice_6(arg,expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(-1.0,1.0),0.0],[(0.4,0.6),1.0]])
def test_add_float_excercice_6(arg,expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("x", [0,5,10])
def test_factorial_excercice_6(x):
    assert calculator.factorial(x) == math.factorial(x)

@pytest.mark.parametrize("theta, N, value", [(0,0,0),(1,4,0.84147)])
def test_sin_excercice_6(theta,N,value):
    assert math.isclose(calculator.sin(theta,N), value, rel_tol=0.001)

@pytest.mark.parametrize("x,y,ans",[(2,2,1),(3,2,1.5)])
def test_divide_excercice_6(x,y,ans):
    assert math.isclose(calculator.divide(x,y), ans, rel_tol=0.001)

@pytest.mark.parametrize("x,xfac",[(1,1),(4,8),(5,15)])
def test_double_factorial_excercice_6(x,xfac):
    assert calculator.double_factorial(x) == xfac

@pytest.mark.parametrize("x,xabs",[(1,1),(-42,42),(0,0)])
def test_absolute_value_excercice_6(x,xabs):
    assert calculator.absolute_value(x) == xabs