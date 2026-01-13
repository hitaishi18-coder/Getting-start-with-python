# you are preparing an order summary with customer names and their total __build_class__

# task :
#     use two lists: one for names and one for __build_class__
#     print : '[name] and paid rs[amount]'

names = ["hitesh","meera","sam","ali"]
bills = [50, 60, 70, 100]

for name , amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
    