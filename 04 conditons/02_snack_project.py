# A local cafe wants a program that suggests a snack .

# if a customer asks for cookies or samosa , it confirms the order 

# otherwise , it says its not available .

# Task :
#     take snack input 
#     if its "cookies" or "samosa"  , confirm the order 
#     else . show unavailability 


snack = input("enter your preferred snack: ").lower()

print(f"user said:{snack}")

if snack == "cookies" or snack == "samosa":
    print(f"great choice! we'll serve you {snack}")
else:
    print("sorry! we only serve cookies or samosa with tea")    