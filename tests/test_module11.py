import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module11_web_apis as m


def test_extract_user_url():
    assert m.extract_user_url({'rate_limit_url': 'https://api.github.com/rate_limit'}) == 'https://api.github.com/rate_limit'
    assert m.extract_user_url({'other': 'value'}) is None


def test_parse_html_title():
    html = '<html><head><title>Test</title></head><body></body></html>'
    assert m.parse_html_title(html) == 'Test'


def test_weather_summary():
    summary = m.format_weather_summary({'location': 'Paris', 'temp_c': 18, 'condition': 'Sunny'})
    assert 'Paris' in summary
    assert '18' in summary
