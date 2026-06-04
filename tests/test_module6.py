import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module6_file_io_errors as m


def test_write_and_read_notes(tmp_path):
    file_path = tmp_path / 'notes.txt'
    assert m.write_notes(['a\n', 'b\n'], file_path)
    assert m.read_notes(file_path) == ['a', 'b']
    assert m.safe_read(file_path) == 'a\nb\n'


def test_safe_read_missing_file(tmp_path):
    missing = tmp_path / 'missing.txt'
    assert m.safe_read(missing) is None


def test_parse_integer():
    assert m.parse_integer('10') == 10
    assert m.parse_integer('x') is None
