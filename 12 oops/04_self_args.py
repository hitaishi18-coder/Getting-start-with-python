class Chaicup:
    size = 150  # ml
    quantity = "normal"

    def describe(self):
        return f"A {self.size}ml {self.quantity} chai cup"

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))


cup_two = Chaicup()
cup_two.size = "medium "
print(Chaicup.describe(cup_two))