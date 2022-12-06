"""
Database layer
"""
from datetime import date

files = []


def new_file(title):
    try:
        with open(f'{title}.txt', 'x'):
            dt = date.today()
            files.append(f'{title} {dt}')
            return True

    except FileExistsError:
        return False


def read_file(num):

    with open(f'{files[int(num) - 1]}.txt') as file:
        return file.read()


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
            # files.append(dict_list)
            # # Append user dict to global variable notes_an_lists
            #
            # file.write(f'{files}\n')

    except FileExistsError:
        return False


def new_note(title):
    # dict_note = {}
    # dt = date.today()
    # dict_note[title] = f'{title} {dt}'

    while True:
        try:
            with open(f'{title}.txt', 'x'):
                pass
                # dict_note['Note: '] = note
                #
                # files.append(dict_note)
                # file.write(f'{files}\n')

        except FileExistsError:
            return False
