# -------- Example 1: Immutable type (String) --------

chai = "ginger chai"

def prepare_chai(order):
    print("preparing", order)

prepare_chai(chai)
print(chai)   # String is immutable → original value unchanged


print("--------------------------")


# -------- Example 2: Mutable type (List) --------

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 32   # Modifying list element

edit_chai(chai)
print(chai)   # List is mutable → original list gets changed


print("--------------------")


# -------- Example 3: Positional and Keyword Arguments --------

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# Positional arguments: order matters
make_chai("darjeeling", "yes", "low")

# Keyword arguments: order does not matter
make_chai(tea="green", sugar="medium", milk="no")


print("--------------------")


# -------- Example 4: *args and **kwargs --------

def special_chai(*ingredients, **extras):
    # *ingredients → collects extra positional arguments as a tuple
    # **extras → collects extra keyword arguments as a dictionary
    print("ingredients:", ingredients)
    print("extras:", extras)

special_chai("cinnamon", "cardamom", sweetener="honey", foam="yes")


print("-------------------")


# -------- Example 5: Default Argument with None (Best Practice) --------

def chai_order(order=None):
    # Avoid using mutable objects as default arguments
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()

print("-----------------")
