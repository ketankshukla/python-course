def format_requirements(packages):
    return '\n'.join(packages) + '\n'


def package_structure(package_name):
    return [f'{package_name}/', f'{package_name}/__init__.py', 'pyproject.toml']


def parse_requirements(text):
    return [line.strip() for line in text.splitlines() if line.strip()]
