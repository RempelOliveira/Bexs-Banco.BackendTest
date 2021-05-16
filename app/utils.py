import os


def clear_screen():
    os.system('clear')


def format_price(price):
    return '{:.2f}'.format(price).replace('.', ',')


def has_duplicates(items):
    return len(items) != len(set(items))
