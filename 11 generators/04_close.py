# -------- Example 1: yield from (Generator Delegation) --------

def local_chai():
    yield "masala chai"
    yield "ginger chai"

def imported_chai():
    yield "matcha"
    yield "oolong"

def full_menu():
    # yield from automatically iterates through another generator
    yield from local_chai()
    yield from imported_chai()

# Iterating through combined generator
for chai in full_menu():
    print(chai)


print("--------------------")


# -------- Example 2: Generator cleanup using close() --------

def chai_stall():
    try:
        while True:
            # Generator waits for orders
            order = yield "watching for chai order"
    except GeneratorExit:
        # Runs when stall.close() is called
        print("stall closed, no more chai")

# Create generator
stall = chai_stall()

# Start generator to first yield
print(next(stall))

# Close generator (triggers GeneratorExit)
stall.close()
