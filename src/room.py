# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, rm_name, rm_description):
        self.rm_name = rm_name
        self.rm_description = rm_description

    def __str__(self):
        return f"<Room name: {self.rm_name}> "
