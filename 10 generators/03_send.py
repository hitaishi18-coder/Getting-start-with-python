# -------- Generator used as a Coroutine --------

def chai_customer():
    # First message when generator starts
    print("welcome ! what chai would you like ? ")
    
    # yield waits to RECEIVE a value using send()
    order = yield  
    
    # Infinite loop to keep taking new orders
    while True:
        print(f"preparing : {order} ")
        
        # Wait for next order
        order = yield


# Create generator object
stall = chai_customer()

# Start the generator
# This runs code until first 'yield'
next(stall)

# Send orders into the generator
stall.send("masala tea")
stall.send("lemon chai")
