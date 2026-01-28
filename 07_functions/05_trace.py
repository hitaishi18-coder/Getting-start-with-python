# Function to add VAT (tax) to a given price
# price → original price of the item
# vat_rate → VAT percentage to be added
# The function returns the final price including VAT
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

# List of order prices (original prices)
orders = [100, 150, 200]

# Loop through each order price
for price in orders:
    # Calculate final amount after adding 10% VAT
    final_amount = add_vat(price, 10)
    
    # Print original and final price
    print(f"original: {price}, final with VAT : {final_amount}")
