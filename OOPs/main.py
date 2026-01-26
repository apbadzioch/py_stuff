from inventory import Inventory
from items.consumables import Potion

my_bag = Inventory()
heal = Potion("Health", 1, 50)
my_bag.add_item(heal)