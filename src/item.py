class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.price = item_description

    def take_item(self):
        print(f"You have added {self.item_name} to your inventory.")

    def drop_item(self):
        print(f"You have dropped: {self.item_name} from your inventory")
