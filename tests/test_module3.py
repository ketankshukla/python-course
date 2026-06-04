import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module3_control_flow as m


def test_grade_letter():
    assert m.grade_letter(95) == 'A'
    assert m.grade_letter(82) == 'B'
    assert m.grade_letter(73) == 'C'
    assert m.grade_letter(60) == 'D'


def test_fizzbuzz():
    assert m.fizzbuzz(5) == [1, 2, 'Fizz', 4, 'Buzz']


def test_is_prime():
    assert m.is_prime(13) is True
    assert m.is_prime(12) is False


def test_summarize_scores():
    summary = m.summarize_scores([70, 80, 90])
    assert summary['count'] == 3
    assert summary['min'] == 70
    assert summary['max'] == 90
    assert summary['average'] == 80
