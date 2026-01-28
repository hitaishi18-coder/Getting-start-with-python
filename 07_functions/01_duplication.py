# This function takes two parameters: name and chai_type
# It prints a message showing who ordered which type of chai
def print_order(name, chai_type):
    # f-string is used to insert variables directly into the string
    print(f"{name} ordered {chai_type} chai !")

# Calling the function with arguments:
# name = "Aman", chai_type = "masala"
print_order("Aman", "masala")

# name = "hitesh", chai_type = "ginger"
print_order("hitesh", "ginger")

# name = "jia", chai_type = "tulsi"
print_order("jia", "tulsi")
