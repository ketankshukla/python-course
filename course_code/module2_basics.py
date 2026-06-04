def simple_calculator(x, y):
    return {
        'sum': x + y,
        'difference': x - y,
        'product': x * y,
        'quotient': x / y if y != 0 else None,
        'floor_div': x // y if y != 0 else None,
        'remainder': x % y if y != 0 else None,
    }


def transform_string(s):
    return {
        'capitalized': s.capitalize(),
        'replaced': s.replace('python', 'code'),
        'length': len(s),
    }


def to_int(value):
    return int(value)


def to_float(value):
    return float(value)


def formatted_message(name, age):
    return f'Name: {name}, age: {age}'
