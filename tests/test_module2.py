import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module2_basics as m


def test_simple_calculator():
    result = m.simple_calculator(10, 3)
    assert result['sum'] == 13
    assert result['difference'] == 7
    assert result['product'] == 30
    assert result['quotient'] == 10 / 3
    assert result['floor_div'] == 3
    assert result['remainder'] == 1


def test_transform_string():
    data = m.transform_string('learn python')
    assert data['capitalized'] == 'Learn python'
    assert data['replaced'] == 'learn code'
    assert data['length'] == len('learn python')


def test_conversion_helpers():
    assert m.to_int('42') == 42
    assert m.to_float('3.14') == 3.14
    assert m.formatted_message('Sam', 21) == 'Name: Sam, age: 21'
