"""
Presentation layer
"""
from nb_business import create_new_file, read_old_file, update_old_file, get_file_list


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

        if choice == '2':
            files = get_file_list()

            # Display saved files
            for i in enumerate(files, 1):
                print(f'{i[0]}. {i[1]}')

            list_num = input('List/ note #: > ')

            print(read_old_file(list_num))

        if choice == '3':
            files = get_file_list()

            # Display saved files
            for i in enumerate(files, 1):
                print(f'{i[0]}. {i[1]}')

            list_num = input('List/ note to update #: > ')

            title = files[int(list_num)]

            print(read_old_file(list_num))

            data = input('Update item: >')

            update_old_file(title, data)
            print(f'updated')

        if choice == '4':
            print('Delete')


if __name__ == '__main__':
    get_action()
