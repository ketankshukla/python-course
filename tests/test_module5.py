import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module5_functions_modules as m


def test_square_and_introduce():
    assert m.square(5) == 25
    assert m.introduce('Sam', 'Seattle') == 'Sam lives in Seattle.'


def test_min_max_and_count_words():
    assert m.min_max([1, 2, 3]) == (1, 3)
    assert m.count_words('hello world') == 2


def test_describe_and_conversions():
    assert m.describe_pet('Bella', 'cat') == 'Bella is a cat.'
    assert m.celsius_to_fahrenheit(0) == 32
    assert m.fahrenheit_to_celsius(32) == 0
