# ----------------------------
# Example 1: Normal assignment
# ----------------------------

value = 13                      # Store value 13
remainder = value % 5           # Find remainder when 13 is divided by 5 → 3

# If remainder is non-zero, number is not divisible by 5
if remainder:
    print(f"not divisible, remainder is {remainder}")


print("----------------------------------")


# --------------------------------
# Example 2: Using Walrus Operator
# --------------------------------

value = 13

# Walrus operator := assigns and checks in the same line
if (remainder := value % 5):
    print(f"not divisible, remainder is {remainder}")


# ------------------------------------
# Example 3: Walrus with user input
# ------------------------------------

available_size = ["small", "medium", "large"]

# Takes input, stores it in requested_size,
# then checks if it exists in available_size list
if (requested_size := input("Enter your chai cup size: ")) in available_size:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")


# ------------------------------------
# Example 4: Walrus inside while loop
# ------------------------------------

flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavours:", flavours)

# Takes input, stores in flavour,
# loop continues while flavour is NOT in flavours list
while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

# When correct flavour is entered, loop ends
print(f"You chose {flavour} chai ☕")
