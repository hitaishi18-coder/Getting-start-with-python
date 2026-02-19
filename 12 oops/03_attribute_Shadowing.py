# 'Chai' naam ki ek class banayi
class Chai:
    # Yeh Class Variables hain. Default roop se har chai "hot" aur "strong" hogi.
    temperature = "hot"
    strength = "strong"

# 'cutting' naam ka ek object banaya 'Chai' class se
cutting = Chai()

# 'cutting' ke paas khud ka temperature nahi hai, toh usne Class wala "hot" utha liya
# Output: hot
print(cutting.temperature)


# Yahan humne 'cutting' object ke liye ek apna personal (Instance) variable bana diya.
# Ab yeh Class wale "hot" ko ignore karega.
cutting.temperature = "mild"

# Yahan humne ek naya variable 'cup' sirf is 'cutting' object mein add kar diya.
# Class 'Chai' ko is 'cup' ke baare mein kuch nahi pata.
cutting.cup  = "small"

# Ab dono personal variables print honge
# Output: after changing mild
print("after changing", cutting.temperature)
# Output: cup size is  small
print("cup size is ", cutting.cup)


# 'del' keyword variable ko memory se uda deta (delete kar deta) hai
# Isne 'cutting' ka apna personal "mild" temperature delete kar diya
del cutting.temperature

# Isne 'cutting' ka personal "small" cup bhi delete kar diya
del cutting.cup


# ASLI MAGIC YAHAN HOTA HAI!
# Jab humne dobara temperature manga, toh 'cutting' ka personal wala delete ho chuka tha.
# Toh Python wapas Class ('Chai') ke paas gaya aur wahan se default "hot" laakar de diya.
# Output: hot
print(cutting.temperature)

# JABKI YAHAN ERROR AAYEGA! (AttributeError)
# Kyun? Kyunki personal 'cup' ("small") delete ho chuka hai, aur Class ('Chai') mein 'cup' naam ki koi cheez pehle se bani hi nahi thi.
# Jab Python ko dono jagah variable nahi mila, toh code crash ho jayega.
print(cutting.cup)