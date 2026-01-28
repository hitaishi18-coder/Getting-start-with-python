# -------- Example 1: Generator function using yield --------

def serve_chai():
    yield "cup 1 : masala chai"
    yield "cup 2 : ginger chai"
    yield "cup 3 : elaichi chai"

# Calling generator function returns a generator object
stall = serve_chai()


# -------- Example 2: Normal function returning list --------

def get_chai_list():
    # Returns all values at once as a list
    return ["cup1", "cup2", "cup3"]

# Calling list function
print(get_chai_list())   # Prints full list immediately


# -------- Example 3: Generator function --------

def get_chai_generator():
    # Produces values lazily (one at a time)
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

# Calling generator function returns generator object
print(get_chai_generator())   # Prints generator object reference

# Create generator object
chai = get_chai_generator()

# next() fetches the next yielded value from generator
print(next(chai))  # cup 1
print(next(chai))  # cup 2
print(next(chai))  # cup 3
