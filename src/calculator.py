"""
Simple Calculator Module
Provides basic arithmetic operations
"""


class Calculator:
    """Calculator class with basic operations"""

    def __init__(self):
        """Initialize calculator"""
        self.history = []

    def add(self, a, b):
        """
        Add two numbers

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """
        Subtract b from a

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """
        Multiply two numbers

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result

    def divide(self, a, b):
        """
        Divide a by b

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")

        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result

    def power(self, a, b):
        """
        Calculate a raised to power b

        Args:
            a: Base
            b: Exponent

        Returns:
            a raised to power b
        """
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def get_history(self):
        """
        Get calculation history

        Returns:
            List of all calculations
        """
        return self.history

    def clear_history(self):
        """Clear calculation history"""
        self.history = []


# Simple functions for basic operations
def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Calculate a raised to power b"""
    return a ** b


if __name__ == "__main__":
    # Demo
    calc = Calculator()

    print("Calculator Demo")
    print("=" * 40)

    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 × 7 = {calc.multiply(6, 7)}")
    print(f"15 ÷ 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")

    print("\nHistory:")
    for item in calc.get_history():
        print(f"  {item}")