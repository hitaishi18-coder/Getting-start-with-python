# -------- Example 1: Pure Function --------
# A pure function:
# - Does not depend on external variables
# - Does not change external state
# - Always gives same output for same input

def pure_chai(cups):
    return cups * 10

total_chai = 0   # Global variable (external state)


# -------- Example 2: Impure Function --------
# This function changes external state using global variable
# Hence, it is an impure function (side effects)

def impure_chai(cups):
    global total_chai
    total_chai += cups   # Modifies global variable


# -------- Example 3: Recursion --------
# A function calling itself until a base condition is met

def pour_chai(n):
    print(n)

    if n == 0:                 # Base condition
        return "all cups poured"
    
    return pour_chai(n - 1)    # Recursive call

# Calling recursive function
print(pour_chai(3))
