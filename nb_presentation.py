"""
Presentation layer
"""
from nb_business import create_new_file, read_old_file, update_old_file, delete_old_file, get_file_list


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

            if create_new_file(title):
                print(f"File '{title}' created!")
            else:
                print('File name already exists! Try Again!')

        if choice == '2':
            files = get_file_list()

            # Display saved files
            for i in enumerate(files, 1):
                print(f'{i[0]}. {i[1]}')

            list_num = int(input('List/ note #: > '))

            if read_old_file(list_num):
                print(read_old_file(list_num))
            else:
                print('No such file! Try Again!')

        if choice == '3':
            files = get_file_list()

            # Display saved files
            for i in enumerate(files, 1):
                print(f'{i[0]}. {i[1]}')

            list_num = input('List/ note to update #: > ')

            title = files[int(list_num) - 1]

            print(read_old_file(list_num))

            data = input('Update item: >')

            update_old_file(title, data)
            print(f'{title} updated!')

        if choice == '4':
            files = get_file_list()

            # Display saved files
            for i in enumerate(files, 1):
                print(f'{i[0]}. {i[1]}')

            list_num = input('List/ note to delete #: > ')

            title = files[int(list_num) - 1]

            print(read_old_file(list_num))

            delete_old_file(title)

            print(f'{title} deleted!')


if __name__ == '__main__':
    get_action()
