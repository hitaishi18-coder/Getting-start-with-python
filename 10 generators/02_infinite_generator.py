# -------- Infinite Generator Example --------

def infinite_chai():
    count = 1
    while True:                 # Infinite loop
        yield f"Refill #{count}" # Produce one value at a time
        count += 1               # Increase count for next refill

# Each call creates a separate independent generator
refill = infinite_chai()
user2 = infinite_chai()

# Get first 5 refills for refill generator
for _ in range(5):
    print(next(refill))

print("-------------------")

# Get first 6 refills for user2 generator
for _ in range(6):
    print(next(user2))
