orders = ["masala", "ginger"]

try:
    print(orders[2])
except IndexError:
    print("No such order exists!")
