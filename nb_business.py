"""
Business layer
"""
from nb_database import new_file, read_file, files


def get_file_list():
    return files


def create_new_file(title):
    if new_file(title):
        return f"File '{title}' created!"
    return 'File name already exists! Try Again!'


def read_old_file(num):
    return read_file(num)


def update_old_file():
    pass


def delete_old_file():
    pass

# choice = input('1. List\n2. Note\n >')
# new_list = []
# a = 0

# if choice == '1':
#     if new_list(title):
#         return 'List created!'
#     return 'File name exists! Try Again!'
#
# if choice == '2':
#     if new_note(title):
#         return 'Notes created!'
#     return 'File name exists! Try Again!'

# while True:
#     title = input('Title: > ')
#
#     if choice == '1':
#         while True:
#             list_item = input(f'Item: >')
#             if list_item == '':
#                 break
#             new_list.append(list_item)
#
#             a = create_new_list(title, new_list)
#
#     if choice == '2':
#         item = input('Note: >')
#         new_list.append(item)
#
#         a = create_new_note(title, new_list)
#
#     if a == 'No file':
#         print('\nSuch file name already exists!')
#         continue
#
# return 'Created!'
