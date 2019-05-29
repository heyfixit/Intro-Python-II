from room import Room
from player import Player
import random
import textwrap
from item import Item
from termcolor import colored

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
                     [Item(*v) for v in random.sample(items,2)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item(*v) for v in random.sample(items,2)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item(*v) for v in random.sample(items,2)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item(*v) for v in random.sample(items,2)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item(*v) for v in random.sample(items,2)]),
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
# * Prints the current room name
    print(colored(player.current_room.name, 'cyan'))
# * Prints the current description (the textwrap module might be useful here).
    print(textwrap.fill(player.current_room.description, 70), '\n')

    print("Items:")
    for item in player.current_room.items:
        print(item)
# * Waits for user input and decides what to do.
    cmd = input("\nInput Command: ")
    print(cmd)

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
    while(cmd != 'q' and (not hasattr(player.current_room, f"{cmd}_to")
                          or getattr(player.current_room, f"{cmd}_to")) is None):
        print("Nothing in that direction")
        cmd = input("Input Command: ")


# If the user enters "q", quit the game.
    if(cmd == 'q'):
        exit()

    player.current_room = getattr(player.current_room, f"{cmd}_to")
