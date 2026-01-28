def brew_chai(flavor):
    
    # Check if flavor is supported
    if flavor not in ["masala", "ginger", "elaichi"]:
        
        # If not supported, manually raise an exception
        raise ValueError("Unsupported chai flavor")
    
    # If no exception, normal execution
    print(f"Brewing {flavor} chai..")


# -------------------------
# Function calls
# -------------------------

brew_chai("masala")   # Works fine

brew_chai("mint")     # Raises ValueError
