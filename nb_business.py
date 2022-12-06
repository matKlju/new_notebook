"""
Business layer
"""
from nb_database import new_file, read_file, update_file, files


def create_new_file(title):
    if new_file(title):
        return f"File '{title}' created!"
    return 'File name already exists! Try Again!'


def get_file_list():
    return files


def read_old_file(num):
    return read_file(num)


def update_old_file(title, data):
    update_file(title, data)


def delete_old_file():
    pass
