# 'A' humari sabse Badi Parent Class (Grandparent) hai
class A:
    label = "A: Base class"

# 'B' ne 'A' ki virasat li aur apna label badal diya
class B(A):
    label = "B: Masala blend"

# 'C' ne bhi 'A' ki virasat li aur isne bhi apna label badal diya
class C(A):
    label = "C: Herbal blend"

# ASLI TWIST YAHAN HAI: The Diamond Problem 💎
# 'D' ne ek saath 'C' aur 'B' dono se inheritance li hai. 
# Kyunki iska structure diagram mein ek Diamond jaisa banta hai (A upar, B aur C beech mein, D neeche), isko Diamond Problem kehte hain.
class D(C, B):
    # 'D' ke paas apna koi label nahi hai
    pass

# Humne 'D' ka ek object banaya 'cup'
cup = D()

# Ab Python ke samne dharam-sankat (confusion) hai:
# 'D' mein label nahi hai, toh wo kahan jaye? 'C' ke paas (Herbal) ya 'B' ke paas (Masala)?
# Is confusion ko dur karne ke liye Python ek strict rule follow karta hai: MRO (Left-to-Right).
# Kyunki 'class D(C, B):' mein 'C' pehle (left mein) likha hai, Python pehle 'C' ke paas jayega!
# Output: C: Herbal blend
print(cup.label)


# __mro__ (Method Resolution Order) Python ka ek jasoosi tool hai.
# Yeh humein batata hai ki variable ya function dhoondhne ke liye Python kis raste (order) se jayega.
# Output: (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# Iska matlab: Pehle 'D' mein dekho -> fir Left parent 'C' -> fir Right parent 'B' -> fir Grandparent 'A' -> aakhiri mein default 'object'.
print(D.__mro__)