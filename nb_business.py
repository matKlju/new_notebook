"""
Business layer
"""
from nb_database import create_new_list, create_new_note


def new_item(a, title, items):
    if a == '1':
        create_new_list(title, items)
    if a == '2':
        create_new_note(title.items)
