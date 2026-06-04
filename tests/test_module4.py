import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module4_data_structures as m


def test_tuple_from_list():
    assert m.tuple_from_list(['a', 'b']) == ('a', 'b')


def test_set_operations():
    ops = m.set_operations({1, 2}, {2, 3})
    assert ops['intersection'] == {2}
    assert ops['union'] == {1, 2, 3}
    assert ops['difference'] == {1}


def test_phonebook_lookup():
    assert m.phonebook_lookup({'Ava': '555'}, 'Ava') == '555'
    assert m.phonebook_lookup({'Ava': '555'}, 'Sam') is None


def test_inventory_summary():
    assert m.inventory_summary([{'qty': 4}, {'qty': 3}]) == 7
