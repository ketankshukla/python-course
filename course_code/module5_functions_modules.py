def square(x):
    return x * x


def introduce(name, city='Unknown'):
    return f'{name} lives in {city}.'


def min_max(values):
    return min(values), max(values)


def count_words(text):
    return len(text.split())


def describe_pet(name, species='dog'):
    return f'{name} is a {species}.'


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
