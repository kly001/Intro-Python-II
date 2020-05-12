# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, player_name, player_location):
        self.player_name = player_name
        self.player_location = player_location
