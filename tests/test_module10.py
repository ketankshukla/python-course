import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module10_data as m


def test_csv_and_json_workflow(tmp_path):
    csv_path = tmp_path / 'grades.csv'
    rows = [['name', 'score'], ['Ava', '92'], ['Ben', '85']]
    assert m.write_csv(csv_path, rows)
    assert m.read_csv_average(csv_path) == (92 + 85) / 2

    json_path = tmp_path / 'contact.json'
    assert m.save_json(json_path, {'name': 'Leo'})
    assert m.load_json(json_path)['name'] == 'Leo'


def test_sales_summary():
    summary = m.sales_summary([
        {'quantity': 2, 'price': 10.0},
        {'quantity': 1, 'price': 5.0},
    ])
    assert summary['total'] == 25.0
    assert summary['average'] == 12.5
