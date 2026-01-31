def cake_customer():
    print("welcome ! what cake order you want for your party ? ")
    order = yield
    while True:
        print(f"preparing... {order}")
        order = yield

cakes = cake_customer()
next(cakes)

cakes.send("chocolate cake")
cakes.send("cheese cake")