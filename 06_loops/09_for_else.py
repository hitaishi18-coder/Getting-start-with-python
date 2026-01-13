staff = [("amit",16),("zara, 17"),("raj",15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else :
    print(f"no one is eligible to manage the staff")