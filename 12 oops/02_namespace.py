# 'Chai' naam ki ek class (blueprint) banayi
class Chai:
    # Yeh ek 'Class Variable' hai. 
    # Iska matlab hai ki is class se banne wali har chai ka origin default roop se "india" hi hoga.
    origin = "india"

# Bina koi object banaye hum seedha class ka data print kar sakte hain
# Output: india
print(Chai.origin)

# Python mein hum class banne ke baad bhi usme naye variable add kar sakte hain
# Yahan humne ek naya rule bana diya: Har chai by default garam (True) hogi
Chai.is_hot = True

# Ab humne 'Chai' class se ek asli object banaya aur use 'masala' naam diya
masala = Chai()

# 'masala' object ke paas khud ka 'origin' nahi tha, toh usne Class wala 'india' utha liya
# Output: masala india
print(f"masala {masala.origin}")

# Same yahan, 'masala' ke paas khud ka 'is_hot' nahi tha, toh usne Class wala 'True' utha liya
# Output: masala True
print(f"masala {masala.is_hot}")

# YAHAN ASLI KHEL HAI! 
# Yahan humne Class ka data change NAHI kiya. 
# Humne sirf is 'masala' object ke andar ek personal (Instance) variable bana diya aur use False kar diya.
masala.is_hot = False

# Check karte hain ki kya Class wali default chai abhi bhi garam hai?
# Haan! Class ka data safe hai. Output: masala True
print(f"masala", Chai.is_hot)

# Check karte hain ki kya humari specific 'masala' chai thandi hui?
# Haan! Isne apna personal variable use kiya. Output: masala False
print(f"masala {masala.is_hot}")

# Hum kisi specific object mein ek bilkul naya personal variable bhi add kar sakte hain bahar se
# Yeh 'flavor' sirf aur sirf is 'masala' object ke paas hai, Class ko iske baare mein nahi pata
masala.flavor = "masala"

# Personal variable ko print kiya
# Output: masala
print(masala.flavor)