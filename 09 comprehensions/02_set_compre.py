cakes = [
    "cheese cake" , "truffle cake", "dry cake",
    "pineapple cake" , "blueberry cake" , "dark chocolate cake"
]

unique_cake = [cake for cake in cakes]
print(unique_cake)


my_bake = {
    "cake" : ["choco lava", "truffle", "pineapple"],
    "pastry" : ["vanila","strawbeerry", "jam roll"],
    "bakes" : ["patty" , "cream roll" , "finger"]
}

varieties = [bake for bake in my_bake.values() for bake in bake]
print(varieties)