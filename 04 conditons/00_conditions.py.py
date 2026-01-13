# -------- IF STATEMENT --------

a = 33
b = 200

if b > a:
    # Executes when condition is True
    print("b is greater than a!")


number = 15
if number > 0:
    # Checks if number is positive
    print("the number is positive")


# -------- IF BLOCK --------

age = 20
if age >= 18:
    # Multiple statements inside if block
    print("you are an adult")
    print("you can vote")
    print("you have full legal right !")


is_logged_in = True
if is_logged_in:
    # Boolean condition check
    print("welcome back !")


# -------- ELIF --------

a = 33
b = 33

if b > a:
    print("b is greater than a ")
elif a == b:
    # Runs when first condition is False and this one is True
    print("a and b are equal")


score = 75

if score >= 90:
    print("grade A")
elif score >= 80:
    print("grade b")
elif score >= 70:
    print("grade c ")
elif score >= 60:
    print("grade d ")


age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")


day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")


# -------- ELSE KEYWORD --------

a = 200
b = 33

if b > a:
    print("b is greater than a ")
elif a == b:
    print("a and b are equal")
else:
    # Runs when all above conditions are False
    print("a is greater than b ")


a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


number = 7
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd ")


temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside!")


username = "Emil"

if len(username) > 0:
    # f-string for formatted output
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")


# -------- SHORTHAND IF --------

a = 5
b = 2

if a > b: print("a is greater than b")


a = 2
b = 330
print("A") if a > b else print("B")


a = 10
b = 20

bigger = a if a > b else b
# Ternary operator assigns value based on condition
print("bigger is ", bigger)


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


x = 15
y = 20

max_value = x if x > y else y
print("max value :", max_value)


username = ""
display_name = username if username else "guest"
# Empty string is treated as False
print("welcome", display_name)


# -------- LOGICAL OPERATORS --------

a = 200
b = 33
c = 500

if a > b and c > a:
    # AND → both conditions must be True
    print("Both conditions are True")


if a > b or a > c:
    # OR → any one condition must be True
    print("At least one of the conditions is True")


a = 33
b = 200

if not a > b:
    # NOT reverses the condition
    print("a is NOT greater than b")


age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    # Complex logical condition
    print("Discount applies!")


temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")


username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    # Non-empty strings evaluate to True
    print("Login successful")
else:
    print("Login failed")


score = 85

if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")


# -------- NESTED IF --------

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        # Inner if depends on outer if
        print("and also above 20!")
    else:
        print("but not above 20.")


age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")


print("-------")


score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")


temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")


# Same logic using AND operator
if temperature > 20 and is_sunny:
    print("Perfect beach weather!")


# -------- PASS STATEMENT --------

a = 33
b = 200

if b > a:
    pass
# pass does nothing, but avoids syntax error


age = 16

if age < 18:
    pass  # TODO: Add underage logic later
else:
    print("Access granted")


score = 85

if score > 90:
    pass
print("Score processed")


value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass
else:
    print("Positive value")


def calculate_discount(price):
    pass
# Function exists but logic will be added later


# -------- MATCH STATEMENT (Python 3.10+) --------

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        # Default case
        print("Looking forward to the Weekend")


day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")


month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
