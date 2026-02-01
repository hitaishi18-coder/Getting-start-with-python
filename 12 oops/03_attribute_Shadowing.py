class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)


cutting.temperature = "mild"
cutting.cup  = "small"
print("after changing", cutting.temperature)
print("cup size is ", cutting.cup)

del cutting.temperature
del cutting.cup

print(cutting.temperature)
print(cutting.cup)