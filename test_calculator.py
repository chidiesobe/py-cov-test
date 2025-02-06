import pytest
from calculator import add, subtract, multiply, divide, Calculator

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(1, 0)

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_square(self):
        assert self.calc.square(2) == 4
        assert self.calc.square(-2) == 4
        assert self.calc.square(0) == 0
    
    def test_cube(self):
        assert self.calc.cube(2) == 8
        assert self.calc.cube(-2) == -8
        assert self.calc.cube(0) == 0
    
    def test_power(self):
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(2, 0) == 1
        assert self.calc.power(0, 5) == 0