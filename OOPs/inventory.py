class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print(f"Added {item.name} to inventory.")

    def use_all_items(self):
        for item in self.__items:
            print(item.use())