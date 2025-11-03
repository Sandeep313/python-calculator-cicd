"""
Test suite for calculator module
"""
import pytest
from src.calculator import Calculator, add, subtract, multiply, divide, power


class TestCalculatorClass:
    """Test Calculator class"""

    def test_add(self):
        """Test addition"""
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
        assert calc.add(100, 200) == 300

    def test_subtract(self):
        """Test subtraction"""
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(10, 15) == -5
        assert calc.subtract(0, 0) == 0

    def test_multiply(self):
        """Test multiplication"""
        calc = Calculator()
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(10, 10) == 100

    def test_divide(self):
        """Test division"""
        calc = Calculator()
        assert calc.divide(10, 2) == 5
        assert calc.divide(9, 3) == 3
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_power(self):
        """Test power operation"""
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(10, 2) == 100
        assert calc.power(2, 10) == 1024

    def test_history(self):
        """Test calculation history"""
        calc = Calculator()

        calc.add(2, 3)
        calc.multiply(4, 5)

        history = calc.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history[0]
        assert "4 × 5 = 20" in history[1]

    def test_clear_history(self):
        """Test clearing history"""
        calc = Calculator()

        calc.add(1, 1)
        calc.multiply(2, 2)

        assert len(calc.get_history()) == 2

        calc.clear_history()
        assert len(calc.get_history()) == 0


class TestSimpleFunctions:
    """Test simple calculator functions"""

    def test_add_function(self):
        """Test add function"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0

    def test_subtract_function(self):
        """Test subtract function"""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5

    def test_multiply_function(self):
        """Test multiply function"""
        assert multiply(3, 4) == 12
        assert multiply(0, 10) == 0

    def test_divide_function(self):
        """Test divide function"""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5

    def test_divide_function_zero(self):
        """Test divide by zero"""
        with pytest.raises(ValueError):
            divide(10, 0)

    def test_power_function(self):
        """Test power function"""
        assert power(2, 3) == 8
        assert power(5, 0) == 1


class TestEdgeCases:
    """Test edge cases"""

    def test_large_numbers(self):
        """Test with large numbers"""
        calc = Calculator()
        result = calc.multiply(1000000, 1000000)
        assert result == 1000000000000

    def test_negative_numbers(self):
        """Test with negative numbers"""
        calc = Calculator()
        assert calc.add(-5, -3) == -8
        assert calc.multiply(-2, -3) == 6
        assert calc.divide(-10, 2) == -5

    def test_floating_point(self):
        """Test with floating point numbers"""
        calc = Calculator()
        assert calc.add(1.5, 2.3) == pytest.approx(3.8)
        assert calc.divide(7, 3) == pytest.approx(2.333, abs=0.01)