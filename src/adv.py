from room import Room
from player import Player

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
player = Player(input("Please tell me your name:  "), current_room = room['outside'])
print(f"Thank you are you ready to begin, {player.name}? Let's go!")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    print(f"{player.name}, you are now: {player.current_room.rm_name}, ({player.current_room.rm_description}!)")
    direction = input("Which direction do you what to go: (n)North, (s)South, (e)East, (w)West, or (q) to Quit the game?  ")


    if direction == "q":
            print("Thanx for playing. Bye for now!")
            break

    try:
        if direction == "n":
            print("I don't think going North is a great idea.  Try again.")
        elif direction == "e":
            print("I don't think going East is a great idea.  Try again.")
        elif direction == "w":
            print("I don't think going West is a great idea.  Try again.")
        elif direction == "s":
            print("I don't think going South is a great idea.  Try again.")
        else:
            print("That's not a valid selection.  Try again")
    except ValueError:
            print("Please make your choice from the directions listed above.")
       
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.


#
# If the user enters "q", quit the game.
