"""
Business layer
"""
from nb_database import new_file, read_file, update_file, delete_file, files


def get_file_list():
    return files


def create_new_file(title):
    return new_file(title)


def read_old_file(num):
    return read_file(num)


def update_old_file(title, data):
    return update_file(title, data)


def delete_old_file(title):
    return delete_file(title)
