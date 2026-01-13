# Function to calculate total bill amount
# It takes:
# cups → number of cups ordered
# price_per_cup → price of one cup
# It returns the total bill
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

# Calling the function and storing the returned value in a variable
my_bill = calculate_bill(3, 16)
print(my_bill)   # Output: total bill for 3 cups at ₹16 each

# Directly calling the function inside print
# Calculates bill for table 2: 2 cups at ₹50 each
print("order for table 2 : ", calculate_bill(2, 50))
