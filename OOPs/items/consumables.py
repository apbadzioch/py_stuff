from items.base import Item

class Potion(Item):
    def __init__(self, name, weight, effect_points):
        super().__init__(name, weight)
        self.effect_points = effect_points

    def use(self):
        return f"Consumed {self.name}. Restored {self.effect_points} HP!"

