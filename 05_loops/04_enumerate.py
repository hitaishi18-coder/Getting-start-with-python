# you are creating a tea menu board.

# each item must be numbered 

# task :
#     use enumerate() to print menu items with numbers..

menu = ["green", "lemon","spiced", "mint"]

for idx , item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai ")