# Matthew Bayers
items = []

def game():
    """
    For the variables, we have a dictionary (rooms) with the rooms and their
    possible directions. Current room holds the current room after moving
    to the next. Counter starts an infinite loop - this is done by setting counter
    not equal to 0, and adding 1 at each iteration. Infinite!
    """
    rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }
    current_room = 'Great Hall'
    counter = 1
    while counter != 0:
        print('You are in the', current_room)
        direction = input('Enter a command.\n')
        direction = direction.split()
        """
        Checking the direction, to see if user would like to exit,
        and breaking if true. Then checking to see if the user input
        includes go, and a direction. Once those parameters are met
        we move into the elif statements and print Direction: xxxxxx,
        and change current_room to the new room after moving in the
        direction. If go is met, and input is invalid ex: 'go Souuth',
        output: 'That is not a valid input'
        """
        if direction[0] == 'exit':
            break
        elif direction[1] in rooms[current_room]:
            if direction[0] == 'go':
                if direction[1] == 'West':
                    print('Direction: West')
                    current_room = (rooms[current_room][direction[1]])
                elif direction[1] == 'East':
                    print('Direction: East')
                    current_room = (rooms[current_room][direction[1]])
                elif direction[1] == 'South':
                    print('Direction: South')
                    current_room = (rooms[current_room][direction[1]])
                elif direction[1] == 'North':
                    print('Direction: North')
                    current_room = (rooms[current_room][direction[1]])
                else:
                    print('That is not a valid input.')
        else:
            print('That is not a valid input.')
        counter += 1


def add_item():
    user_input = input('Would you like to add item to inventory?')
    if user_input == 'yes':
        print('cool!')
        items.append(item)
    elif user_input == 'no':
        print('oh okay')
    else:
        print('That is not a valid input.')
        add_item()


def item_check(item):
    if item in items:
        print('You have already collected the item from this room!\n\n')
        if len(items) == 6:
            win()
            return true
        else:
            print('You have found a', item, 'added to inventory!\n\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
