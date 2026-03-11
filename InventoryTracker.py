class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        self.inventory[item_name] = quantity

    def display_inventory(self):
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")