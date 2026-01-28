# Parent class
class Chai:
    def __init__(self, type_, strength):
        self.type = type_         # Store chai type
        self.strength = strength  # Store chai strength


# ----------------------------------------------------
#  Version 1 (Not ideal)
# Rewriting everything manually
# ----------------------------------------------------
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # Manually setting parent attributes
        # Works, but if parent changes later → problem
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level


# ----------------------------------------------------
# Version 2 (Better, but old-style)
# Calling parent class directly
# ----------------------------------------------------
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # Call parent constructor explicitly
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level


# ----------------------------------------------------
# Version 3 (Best Practice)
# Using super()
# ----------------------------------------------------
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # super() automatically refers to parent class
        super().__init__(type_, strength)
        self.spice_level = spice_level
