"""
Database layer
"""
from datetime import date
import os
import glob

os.chdir(r'C:\Users\Mati\Documents\GitHub\new_notebook')
files = glob.glob('*.txt')


def new_file(title):
    try:
        with open(f'{title}.txt', 'x'):
            files.append(f'{title}')
            return True

    except FileExistsError:
        return False


def read_file(num):
    try:
        with open(f'{files[int(num)]}.txt') as file:
            return file.read()

    except IndexError:
        return False


def update_file(title, data):
    try:
        with open(f'{title}.txt', 'a') as file:
            dt = date.today()
            file.write(f'{data} {dt}\n')
            return True

    except FileExistsError:
        return False


def delete_file(title):
    if os.path.exists(f'{title}.txt'):
        os.remove(f'{title}.txt')
        return True
    else:
        return False

# def new_list(title):
#     # dict_list = {}
#     # dt = date.today()
#     # dict_list['Title'] = f'{title} {dt}'
#
#     try:
#         with open(f'{title}.txt', 'x'):
#             return True
#             # # Write to file.
#             # for i in enumerate(items, 1):
#             #     dict_list[f'{i[0]}.'] = i[1]
#             #     # for loop iterator as a key and item as value
#             #
#             # files.append(dict_list)
#             # # Append user dict to global variable notes_an_lists
#             #
#             # file.write(f'{files}\n')
#
#     except FileExistsError:
#         return False
#
#
# def new_note(title):
#     # dict_note = {}
#     # dt = date.today()
#     # dict_note[title] = f'{title} {dt}'
#
#     while True:
#         try:
#             with open(f'{title}.txt', 'x'):
#                 pass
#                 # dict_note['Note: '] = note
#                 #
#                 # files.append(dict_note)
#                 # file.write(f'{files}\n')
#
#         except FileExistsError:
#             return False
