import csv
import json
from pathlib import Path


def write_csv(path, rows):
    p = Path(path)
    with p.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return p.exists()


def read_csv_average(path):
    p = Path(path)
    with p.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        scores = [int(row['score']) for row in reader]
    return sum(scores) / len(scores) if scores else 0


def save_json(path, data):
    p = Path(path)
    with p.open('w', encoding='utf-8') as f:
        json.dump(data, f)
    return p.exists()


def load_json(path):
    p = Path(path)
    with p.open('r', encoding='utf-8') as f:
        return json.load(f)


def sales_summary(sales):
    total = sum(entry['quantity'] * entry['price'] for entry in sales)
    average = total / len(sales) if sales else 0
    return {'total': total, 'average': average}
