"""
Presentation layer
"""
from nb_business import create_new_file, read_old_file


def get_action():
    choices = ['Create', 'Read',
               'Update', 'Delete']
    
    while True:
        #  Display choices
        for i in enumerate(choices, 1):
            print(f'{i[0]}. {i[1]}')
            
        choice = input('> ')
        choice = choice.lower()
        
        if choice == '1':
            title = input('Title: > ')
            print(create_new_file(title))

        if choice == '2' or choice == 'read':
            print(read_old_file())

        if choice == '3' or choice == 'update':
            print('Update')

        if choice == '4' or choice == 'delete':
            print('Delete')


if __name__ == '__main__':
    get_action()
