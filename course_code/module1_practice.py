def sum_and_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg


def area_of_circle(r, pi=3.14159):
    return pi * r * r


def greet(name):
    return f"Hello, {name}! Welcome to Python."


def count_vowels(text):
    vowels = set('aeiou')
    return sum(1 for ch in text.lower() if ch in vowels)


def even_squares(n=10):
    return [x * x for x in range(1, n + 1) if x % 2 == 0]


def fizzbuzz(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append('FizzBuzz')
        elif i % 3 == 0:
            out.append('Fizz')
        elif i % 5 == 0:
            out.append('Buzz')
        else:
            out.append(i)
    return out


def factorial(n):
    """Return n! for n >= 0 (iterative)."""
    if n < 0:
        raise ValueError('n must be >= 0')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """Return True if n is prime (n >= 2)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards (ignoring case and non-alphanumerics)."""
    import re

    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]
