"""
Database layer
"""
from datetime import date

notes_and_lists = []


def create_new_list(title, items):
    dict_list = {}
    dt = date.today()
    dict_list['Title'] = f'{title} {dt}'

    try:
        with open(f'{title}.txt', 'x') as file:
            # Write to file.
            for i in enumerate(items):
                dict_list[f'{i[0]}.'] = i[1]
                # for loop iterator as a key and item as value

            notes_and_lists.append(dict_list)
            # Append user dict to global variable notes_an_lists

            file.write(f'{notes_and_lists}\n')
            # Write notes_and_list to file

    except FileExistsError:
        print('\nSuch file name already exists!')
        # returns an error if the file exists
        create_new_list()


def create_new_note(title):
    dict_note = {}
    dt = date.today()
    dict_note[title] = f'{title} {dt}'

    try:
        with open(f'{title}.txt', 'x') as file:


                dict_note[f'{i}.'] = note

                notes_and_lists.append(dict_note)
                file.write(f'{notes_and_lists}\n')

    except FileExistsError:
        print('\nSuch file name already exists!')  # returns an error if the file exists
        create_new_list()


def read():
    for i in enumerate(notes_and_lists):
        print(f'{i[0]}. {i[1]}')

    choice = input('Read note: > ')

    try:
        with open(f'{choice}.txt') as file:
            print(file.read())

    except FileNotFoundError:
        print('File not found!')
        read()

