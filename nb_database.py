"""
Database layer
"""
from datetime import date

notes_and_lists = []


def new_file(title):
    try:
        with open(f'{title}.txt', 'x'):
            notes_and_lists.append(f'{title}')
            return True

    except FileExistsError:
        return False


def read_file():
    for i in enumerate(notes_and_lists):
        print(f'{i[0]}. {i[1]}')

    choice = input('Read note: > ')

    try:
        with open(f'{choice}.txt') as file:
            print(file.read())

    except FileNotFoundError:
        print('File not found!')


def new_list(title):
    # dict_list = {}
    # dt = date.today()
    # dict_list['Title'] = f'{title} {dt}'

    try:
        with open(f'{title}.txt', 'x'):
            return True
            # # Write to file.
            # for i in enumerate(items, 1):
            #     dict_list[f'{i[0]}.'] = i[1]
            #     # for loop iterator as a key and item as value
            #
            # notes_and_lists.append(dict_list)
            # # Append user dict to global variable notes_an_lists
            #
            # file.write(f'{notes_and_lists}\n')

    except FileExistsError:
        return False


def new_note(title):
    # dict_note = {}
    # dt = date.today()
    # dict_note[title] = f'{title} {dt}'

    while True:
        try:
            with open(f'{title}.txt', 'x'):

                # dict_note['Note: '] = note
                #
                # notes_and_lists.append(dict_note)
                # file.write(f'{notes_and_lists}\n')

        except FileExistsError:
            return False


