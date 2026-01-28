# List containing number of cups sold each day
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# Generator expression:
# It selects only sales greater than 5
# Then sum() adds them together
total_cups = sum(sale for sale in daily_sales if sale > 5)

# Print total cups sold where sales > 5
print(total_cups)
