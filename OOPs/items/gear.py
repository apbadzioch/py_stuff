class Shield(Item):
    def __init__(self, name, weight, durability):
        super().__init__(name, weight)
        self.durability = durability

    def use(self):
        self.durability -= 10
        return f"Blocked with {self.name}. Durability is now {self.durability}."
