def process_order(item, quantity):
    try:
        # Dictionary lookup for price per chai
        price = {"masala": 20}[item]
        
        # Calculate total cost
        # This may cause TypeError if quantity is not a number
        cost = price * quantity
        
        print(f"Total cost is {cost}")

    # Runs if item key is not found in dictionary
    except KeyError:
        print("Sorry, that chai is not on the menu")

    # Runs if quantity is not a number
    except TypeError:
        print("Quantity must be a number")


# -------------------------
# Function calls
# -------------------------

process_order("ginger", 2)      
# ginger not in menu → KeyError handled

process_order("masala", "two")  
# "two" is a string → TypeError handled

process_order("masala", 2)     
# No error → Total cost is 40
