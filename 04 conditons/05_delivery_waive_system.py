# you run an online tea store 

# if the order amount is more than rs 300 , delivery is free ,
# otherwise , it costs rs 30 

# task : 
#     input : order_amount 
#     use ternary operator to decide delivery fee 


order_amount = int(input("enter the order amount: "))

print(f"order amount: {type(order_amount)} ")

delivery_fees = 0 if order_amount > 300 else 30

print(f"delivery fees is : {delivery_fees}")

