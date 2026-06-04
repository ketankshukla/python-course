import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module1_practice as m


def test_sum_and_average():
    total, avg = m.sum_and_average([2, 5, 7, 11])
    assert total == 25
    assert avg == 6.25


def test_area_of_circle():
    assert abs(m.area_of_circle(5) - 3.14159 * 25) < 1e-6


def test_greet():
    out = m.greet('Tester')
    assert 'Tester' in out and out.startswith('Hello')


def test_count_vowels():
    assert m.count_vowels('Hello World') == 3


def test_even_squares():
    assert m.even_squares(10) == [4, 16, 36, 64, 100]


def test_fizzbuzz():
    expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    assert m.fizzbuzz(15) == expected


def test_factorial_and_prime_and_palindrome():
    assert m.factorial(0) == 1
    assert m.factorial(5) == 120
    assert m.is_prime(2) is True
    assert m.is_prime(15) is False
    assert m.is_prime(97) is True
    assert m.is_palindrome('Racecar') is True
    assert m.is_palindrome('Hello') is False
