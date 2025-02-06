def add(a: float, b: float) -> float:
    return a + b

# def subtract(a: float, b: float) -> float:
#     return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def square(self, number: float) -> float:
        return number * number
    
    def cube(self, number: float) -> float:
        return number * number * number
    
    def power(self, base: float, exponent: int) -> float:
        return base ** exponent