"""
Presentation layer
"""
from nb_business import new_item


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

            structure = input('1. List\n2. Note\n >')
            title = input('Title: > ')
            items = []

            if structure == '1':
                new_list = []
                for i in range(1, 100):
                    list_item = input(f'{i}.item: >')
                    if list_item == 'q':
                        break
                    new_list.append(list_item)

                items.append(new_list)

            if structure == '2':
                item = input('Note: >')
                items.append(item)

            new_item(structure, title, items)

        if choice == '2' or choice == 'read':
            print('Read')

        if choice == '3' or choice == 'update':
            print('Update')

        if choice == '4' or choice == 'delete':
            print('Delete')


if __name__ == '__main__':
    get_action()
