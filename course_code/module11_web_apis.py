from bs4 import BeautifulSoup


def extract_user_url(api_response):
    return api_response.get('rate_limit_url') if isinstance(api_response, dict) else None


def parse_html_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    if soup.title:
        return soup.title.text
    if soup.h1:
        return soup.h1.text
    return None


def format_weather_summary(data):
    return f"Weather in {data['location']}: {data['temp_c']}°C, {data['condition']}" if 'location' in data else ''
