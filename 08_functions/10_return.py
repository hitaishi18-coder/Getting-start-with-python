# -------- Example 1: Return stops function execution --------

def make_chai():
    return "here is your chai"
    print("here is your chai ")   # This line never runs (after return)

return_value = make_chai()
print(return_value)


print("----------------------")


# -------- Example 2: pass (empty function placeholder) --------

def idle_chaiwala():
    pass   # pass means "do nothing"

print(idle_chaiwala())   # Returns None by default


print("--------------")


# -------- Example 3: Returning a value from function --------

def sold_cups():
    return 120   # Function returns an integer

total = sold_cups()
print(total)


print("--------------")


# -------- Example 4: Conditional return --------

def chai_status(cups_left):
    if cups_left == 0:
        return "sorry chai over"   # Early return
    return "chai is ready"         # Runs if condition is false

print(chai_status(0))
print(chai_status(5))


print("--------------")


# -------- Example 5: Multiple return values --------

def chai_report():
    return 100, 20, 10   # sold, remaining, not_paid
    # Actually returns a tuple: (100, 20, 10)

sold, remaining, not_paid = chai_report()

print("sold:", sold)
print("remaining:", remaining)
