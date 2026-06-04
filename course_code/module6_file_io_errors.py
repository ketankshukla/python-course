from pathlib import Path


def write_notes(lines, path='notes.txt'):
    p = Path(path)
    p.write_text(''.join(lines), encoding='utf-8')
    return p.exists()


def read_notes(path='notes.txt'):
    p = Path(path)
    return p.read_text(encoding='utf-8').splitlines()


def safe_read(path='notes.txt'):
    p = Path(path)
    if not p.exists():
        return None
    return p.read_text(encoding='utf-8')


def parse_integer(value):
    try:
        return int(value)
    except ValueError:
        return None
