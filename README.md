# Python Calculator

A simple calculator project with CI/CD pipeline.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide, power)
- Calculation history tracking
- Comprehensive test coverage
- Automated CI/CD with Jenkins

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from src.calculator import Calculator

calc = Calculator()

# Perform operations
result = calc.add(5, 3)
print(f"5 + 3 = {result}")

# View history
print(calc.get_history())
```

## Testing
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src tests/
```

## CI/CD

This project uses Jenkins for continuous integration and delivery.

**Pipeline stages:**
1. Checkout code
2. Install dependencies
3. Run code quality checks
4. Execute unit tests
5. Generate coverage reports
6. Build package
7. Generate reports

## Project Structure