def tuple_from_list(items):
    return tuple(items)


def set_operations(a, b):
    return {
        'intersection': a & b,
        'union': a | b,
        'difference': a - b,
    }


def phonebook_lookup(book, name):
    return book.get(name)


def inventory_summary(inventory):
    total = sum(entry.get('qty', 0) for entry in inventory)
    return total
