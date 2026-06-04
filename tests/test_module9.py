import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module9_testing_debugging as m


def test_math_helpers():
    assert m.add(2, 3) == 5
    assert m.reverse_text('abc') == 'cba'


def test_safe_divide_and_debug():
    assert m.safe_divide(10, 2) == 5
    assert m.safe_divide(10, 0) is None
    try:
        m.debug_function(None)
    except ValueError as exc:
        assert 'must not be None' in str(exc)
    else:
        raise AssertionError('Expected ValueError when debugging None')
