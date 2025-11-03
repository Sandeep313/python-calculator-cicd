"""Test suite for calculator"""
import pytest
from src.calculator import Calculator


class TestCalculator:

    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(10, 15) == -5

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(0, 5) == 0

    def test_divide(self):
        calc = Calculator()
        assert calc.divide(10, 2) == 5
        assert calc.divide(9, 3) == 3

    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_power(self):
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1

    def test_history(self):
        calc = Calculator()
        calc.add(2, 3)
        calc.multiply(4, 5)
        history = calc.get_history()
        assert len(history) == 2