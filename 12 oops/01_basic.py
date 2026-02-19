# Ek khali class (blueprint) banayi 'Chai' naam se
# 'pass' ka matlab hai ki abhi isme koi data ya function nahi daala hai, error se bachne ke liye khali chhod diya
class Chai:
    pass

# Ek aur khali class banayi 'ChaiTime' naam se
class ChaiTime:
    pass

# Yeh check kar raha hai ki 'Chai' class khud kya hai
# Output: <class 'type'> (Kyunki Python mein class khud bhi ek 'type' ka object hoti hai)
print(type(Chai))


# creating object from class 
# Yahan humne 'Chai' class (blueprint) ka use karke ek asli object banaya aur usko 'my_chai' mein store kar diya
my_chai = Chai()

# Yeh check karega ki 'my_chai' variable ke andar kis type ka data hai
# Output: <class '__main__.Chai'> (Matlab yeh Chai class ka object hai)
print(type(my_chai))

# Yahan hum Python se pooch rahe hain: Kya 'my_chai' object ka type 'Chai' class hai?
# Output: True (Haan, bilkul)
print(type(my_chai) is Chai)

# Yahan hum pooch rahe hain: Kya 'my_chai' object ka type 'ChaiTime' class hai?
# Output: False (Nahi, yeh toh Chai class se bana hai)
print(type(my_chai) is ChaiTime)