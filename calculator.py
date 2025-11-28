import os


DEBUG = os.getenv('DEBUG_MODE', 'false').lower() == 'true'


def add(a, b):
    """Return the sum of two numbers."""
    result = a + b
    if DEBUG:
        print(f"DEBUG: {a} + {b} = {result}")
    return result


def subtract(a, b):
    """Return the difference of two numbers."""
    result = a - b
    if DEBUG:
        print(f"DEBUG: {a} - {b} = {result}")
    return result


def multiply(a, b):
    """Return the product of two numbers."""
    result = a * b
    if DEBUG:
        print(f"DEBUG: {a} × {b} = {result}")
    return result


def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    if DEBUG:
        print(f"DEBUG: {a} ÷ {b} = {result}")
    return result


def power(a, b):
    """Return a to the power of b."""
    result = a ** b
    if DEBUG:
        print(f"DEBUG: {a} ** {b} = {result}")
    return result
