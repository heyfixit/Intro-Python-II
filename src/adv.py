from room import Room
from player import Player
import random
import textwrap
from item import Item
from termcolor import colored
from treasure import Treasure

items = [
    [ "item1", "description1" ],
    [ "item2", "description2" ],
    [ "item3", "description3" ],
    [ "item4", "description4" ]
]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [random.choice([Item(*v), Treasure(*v)]) for v in random.sample(items,2)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [random.choice([Item(*v), Treasure(*v)]) for v in random.sample(items,2)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [random.choice([Item(*v), Treasure(*v)]) for v in random.sample(items,2)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [random.choice([Item(*v), Treasure(*v)]) for v in random.sample(items,2)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [random.choice([Item(*v), Treasure(*v)]) for v in random.sample(items,2)]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('dude', room['outside'])

while True:

# Write a loop that:
#
    print(colored("--------------------------", "magenta"))
# * Prints the current room name
    print(colored(player.current_room.name, 'cyan'))
# * Prints the current description (the textwrap module might be useful here).
    print(textwrap.fill(player.current_room.description, 70))
    print(colored(player.current_room.available_directions(), 'cyan'), '\n\n')

    print(colored( "Room Items:", "yellow" ))
    for item in player.current_room.items:
        print(item)

    # print(colored("\nInventory: ", 'yellow'))
    # for item in player.items:
    #     print(item)
# * Waits for user input and decides what to do.
    split_user_input = input("\nInput Command: ").split(" ")
    verb = split_user_input[0]
    obj = split_user_input[1] if len(split_user_input) > 1 else None

    while(verb == 'i' or verb == 'inventory'):
        print(colored("\nInventory: ", 'yellow'))
        for item in player.items:
            print(item)
        split_user_input = input("\nInput Command: ").split(" ")
        verb = split_user_input[0]
        obj = split_user_input[1] if len(split_user_input) > 1 else None



# If the user enters "q", quit the game.
    if(verb == 'q'):
        exit()


    if(verb == 'get'):
        if obj is None:
            print(colored("Specify item name", 'red'))
            continue

        item = player.current_room.remove_item(obj)
        if not item:
            print(colored("Item does not exist in room", 'red'))
            continue

        player.add_item(item)
        continue

    if(verb == 'drop'):
        if obj is None:
            print(colored("Specify item name", 'red'))
            continue

        item = player.drop_item(obj)
        if not item:
            print(colored("Item does not exist in inventory", 'red'))
            continue

        player.current_room.items.append(item)
        continue



#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
    if(not hasattr(player.current_room, f"{verb}_to")
                   or getattr(player.current_room, f"{verb}_to") is None):
        print(colored("Nothing in that direction", 'red'))
        continue


    player.current_room = getattr(player.current_room, f"{verb}_to")
