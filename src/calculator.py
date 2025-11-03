"""Simple Calculator with History Tracking"""


class Calculator:
    """Calculator with operation history"""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Subtract b from a"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result

    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result

    def power(self, a, b):
        """Calculate a raised to power b"""
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def get_history(self):
        """Get calculation history"""
        return self.history


if __name__ == "__main__":
    calc = Calculator()
    print("Calculator Demo")
    print("=" * 40)
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 × 7 = {calc.multiply(6, 7)}")
    print(f"15 ÷ 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")