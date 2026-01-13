# some chai flavours are out of stock 

# you want to skip those and stop entirely if someone requests a restricted flavour 

# task :
#    skip if flavour is "out of stock"
#    break if flavour is "discontinued"

flavours = ["ginger", "out of stock" , "lemon" ,"discontinued","tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print(f"{flavour} item found .. ")
print(f"out side of loop")    

