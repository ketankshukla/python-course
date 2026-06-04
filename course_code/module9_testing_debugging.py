def add(a, b):
    return a + b


def reverse_text(text):
    return text[::-1]


def safe_divide(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError):
        return None


def debug_function(value):
    if value is None:
        raise ValueError('value must not be None')
    return value
