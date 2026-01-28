# Custom exception for unavailable chai
class InvalidChaiError(Exception):
    pass


def bill(flavor, cups):
    
    # Price menu
    menu = {"masala": 30, "ginger": 40}
    
    try:
        # Raise custom exception if chai not in menu
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        
        # Raise TypeError if cups is not integer
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        
        # If everything is correct, calculate total
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: Rupees {total}")
    
    # Catch ANY exception (custom or built-in)
    except Exception as e:
        print("Error:", e)
    
    # Always runs
    finally:
        print("Thank you for visiting \n")


# -------------------------
# Function calls
# -------------------------

bill("mint", 2)          # Custom exception

bill("masala", "three") # TypeError

bill("ginger", 3)       # No error
