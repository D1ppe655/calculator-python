def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно!")
    return a / b

def percent(a, b):
    """
    Вычисляет процент.
    Если b = 10 и a = 200, возвращает 20 (10% от 200).
    """
    return (a * b) / 100