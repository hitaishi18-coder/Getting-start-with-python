# List containing different tea items available in the menu
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger chai"
]

# List comprehension to filter out only the iced tea items
# It checks each item in menu, and selects those containing the word "iced"
iced_tea = [my_tea for my_tea in menu if "iced" in my_tea]

# Print the final list of iced teas
print(iced_tea)
