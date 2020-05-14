class Item:
    def __init__(self, name, description):
        self.name = name
        self.price = description

    def __str__(self):
        return self.name
