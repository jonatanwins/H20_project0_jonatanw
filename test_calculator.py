import calculator

def test_add_integers_excercice_1():
    assert calculator.add(1,2) == 3

def test_add_float_excercice_2():
    assert round(calculator.add(0.1,0.2),1) == 0.3