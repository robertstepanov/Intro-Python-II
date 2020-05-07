from room import Room
import cmd
import sys
import textwrap
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

goodies = [
    Item('stick', 'candle')
]


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
player = Player("You", room['outside'])

playing = False


print(player)

# Write a loop that:
#
#

if __name__ == "__main__":
    while not playing:

        print(player.current_room)

        for line in textwrap.wrap(player.current_room.print_description()):
            print(line)

        # item_choice.split(' ')
        # if item_choice[0] == 'take' and item_choice[1] in goodies:
        #     player.get_item(item_choice[1])

    # * Waits for user input and decides what to do.

        choice = input("\nSelect a direction to go or q to quit. ")
        print("\n")

    #
    # If the user enters a cardinal direction, attempt to move to the room there.

        if choice in ['n', 's', 'e', 'w']:
            player.current_room = player.move_to(choice, player.current_room)
            continue
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
        if choice in ['q', 'quit']:
            playing = True
            print("Thanks for playing the game.")
