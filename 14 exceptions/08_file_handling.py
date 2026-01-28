
# Method 1: Manual file handling


file = open("order.txt", "w")  # Open file in write mode

try:
    # Write data into the file
    file.write("Masala chai - 2 cups")

finally:
    # This ALWAYS runs
    # Ensures file is closed even if an error occurs
    file.close()



# Method 2: Using 'with' statement


# 'with' automatically handles opening and closing the file
with open("order.txt", "w") as file:
    file.write("Ginger tea - 4 cups")
# No need to call file.close()
# It closes automatically after this block
