# -------------------------------
# Base class for all chai types
# -------------------------------
class BaseChai:
    
    # Constructor: runs when object is created
    def __init__(self, type_):
        self.type = type_   # Store chai type in the object

    # Method to prepare chai
    def prepare(self):
        print(f"Preparing {self.type} chai....")


# -------------------------------
# MasalaChai inherits from BaseChai
# -------------------------------
class MasalaChai(BaseChai):
    
    # Extra method only for MasalaChai
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


# -------------------------------
# ChaiShop class (a shop that serves chai)
# -------------------------------
class ChaiShop:
    
    # Class variable:
    # This decides which chai class the shop will use
    chai_cls = BaseChai

    def __init__(self):
        # When a shop is created, it creates a chai object
        # self.chai_cls refers to BaseChai here
        self.chai = self.chai_cls("Regular")

    # Method to serve chai
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()   # Call prepare() of chai object


# -------------------------------
# FancyChaiShop inherits ChaiShop
# -------------------------------
class FancyChaiShop(ChaiShop):
    
    # Override chai_cls to use MasalaChai instead of BaseChai
    chai_cls = MasalaChai


# -------------------------------
# Creating objects and running
# -------------------------------

shop = ChaiShop()          # Normal shop → uses BaseChai
fancy = FancyChaiShop()    # Fancy shop → uses MasalaChai

shop.serve()
# Serving Regular chai in the shop
# Preparing Regular chai....

fancy.serve()
# Serving Regular chai in the shop
# Preparing Regular chai....

# Fancy shop's chai object is MasalaChai
# So it can call add_spices()
fancy.chai.add_spices()
# Adding cardamom, ginger, cloves.
