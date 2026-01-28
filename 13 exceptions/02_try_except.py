# Dictionary containing chai menu and their prices
chai_menu = {"masala": 30, "ginger": 40}

try:
    # Trying to access a key incorrectly
    # This is WRONG syntax for dictionary access
    # Correct way is: chai_menu["elaichi"]
    chai_menu("elaichi")

except KeyError:
    # This block runs if a KeyError occurs
    print("The key that you are trying to access does not exist")

# This line always runs if program does not crash
print("Hello chai code")
