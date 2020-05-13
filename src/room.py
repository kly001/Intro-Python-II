# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, rm_name, rm_description, n_to = None, s_to = None, e_to = None, w_to = None):
        self.rm_name = rm_name
        self.rm_description = rm_description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"<Room name: {self.rm_name}> "
