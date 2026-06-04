import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module8_packaging as m


def test_format_requirements():
    output = m.format_requirements(['pytest', 'requests'])
    assert 'pytest' in output
    assert 'requests' in output


def test_package_structure_and_parse():
    pkg = m.package_structure('mypkg')
    assert 'mypkg/__init__.py' in pkg
    assert 'pyproject.toml' in pkg
    assert m.parse_requirements('a\nb\n') == ['a', 'b']
