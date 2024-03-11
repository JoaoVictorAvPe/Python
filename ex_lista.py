import os

def insert(list):
    item = input('Type de item name: ')
    list.append(item)
    print('ADDED')

def delete(list):
    index = input('Type the item index to delete: ')
    try:
        index = int(index)
        del list[index]
    except ValueError:
        print('Input a valid index')
        return None
    except IndexError:
        print('Item does not exist in this index')
        return None
    print('DELETED')

def list_values(list):
    if len(list) > 0:
        for item, value in enumerate(list):
            print(f'{item} - {value}')
        return True
    else:
        print('Empty')
        return False

shopping_list = []

while True:
    print('Select an option below: \n1 - Insert\n2 - Delete\n3 - Get List\n4 - Exit')
    choice = input('')
    try:
        choice = int(choice)
    except:
        os.system('cls')
        print('Only numbers accept\n')
        continue

    if choice < 1 or choice > 4:
        os.system('cls')
        print('Select a valid option\n')
        continue
    
    if choice == 1:
        os.system('cls')
        insert(shopping_list)
        input('')
        os.system('cls')
    elif choice == 2:
        os.system('cls')
        if list_values(shopping_list):
            delete(shopping_list)
        input('')
        os.system('cls')
    elif choice == 3:
        os.system('cls')
        list_values(shopping_list)
        input('')
        os.system('cls')
    else:
        os.system('cls')
        print('Leaving')
        break
    
print('end')

