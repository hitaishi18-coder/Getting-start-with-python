# Yeh humari Parent Class (Papa) hai
class Chai:
    # Papa ke paas chai ki 2 basic properties hain: type aur strength
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# ❌ TARIKA 1: GHALAT TARIKA (Code Repeat Karna)
# Yahan humne Papa wale variables wapas se khud likh diye.
# Yeh programming mein bura mana jata hai kyunki yeh "DRY" (Don't Repeat Yourself) rule todta hai.
# Agar kal ko Papa ki class mein 10 naye variables aa gaye, toh kya yahan sab wapas likhoge? Nahi na!
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level
        

# ⚠️ TARIKA 2: THEEK HAI, PAR BEST NAHI (Hardcoded Parent Name)
# Yahan humne explicitly Papa ki class ka naam 'Chai' likh kar unka __init__ bulaya.
# Problem kya hai? Agar kal ko humne 'Chai' class ka naam badal kar 'Beverage' kar diya, 
# toh humein yahan bhi aakar manually naam change karna padega. 
# Aur agar 2-3 parents hue (Multiple Inheritance), toh yeh tarika fail ho jata hai.
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         # Yahan 'self' manually bhejna padta hai
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


# ✅ TARIKA 3: BEST AUR PROFESSIONAL TARIKA (The super() Hero)
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # 'super()' ka aasan bhasha mein matlab hai: "Mere Parent ko bulao".
        # Isko farq nahi padta ki Parent ka naam 'Chai' hai ya kuch aur. 
        # Yeh automatically Parent class ko dhoondhega, uska __init__ chala dega, 
        # aur sabse achi baat: yeh 'self' khud pass kar deta hai, humein nahi likhna padta!
        super().__init__(type_, strength)
        
        # Parent ne apna basic setup (type aur strength) kar diya...
        # Ab Child apna naya personal variable (spice_level) set kar raha hai.
        self.spice_level = spice_level