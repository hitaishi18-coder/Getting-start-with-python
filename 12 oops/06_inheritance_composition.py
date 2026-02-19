# Yeh Parent Class (Papa) hai. Yeh ek normal chai ka naksha (blueprint) hai.
class BaseChai:    #parent class
    # Constructor: Nayi chai bante hi uski 'type' set kar dega
    def __init__(self, type_):
        self.type = type_

    # Yeh chai banane ka method hai
    def prepare(self):
        print(f"Preparing {self.type} chai....")


# Yeh Child Class (Beta) hai. 
# Bracket () mein BaseChai likhne ka matlab hai ki isne Parent ke features copy kar liye hain (Inheritance).
class MasalaChai(BaseChai):   #inheriting 
    # Iske paas apna khud ka ek extra method bhi hai jo Parent ke paas nahi hai
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


# Yeh dukan (Shop) ka naksha hai
class ChaiShop:
    # Class Variable: Dukan by default 'BaseChai' wale blueprint ko use karegi
    chai_cls = BaseChai

    def __init__(self):
        # COMPOSITION (Asli Jaadoo): Dukan (ChaiShop) ke andar humne ek chai ka object banakar rakh diya.
        # "Dukan HAS-A Chai" (Dukan ke paas ek chai hai).
        self.chai = self.chai_cls("Regular")

    # Dukan ka method jo andar rakhi chai object ka use karta hai
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


# Yeh ek fancy dukan hai jo purani normal dukan ko Inherit kar rahi hai
class FancyChaiShop(ChaiShop):
    # Isne koi naya function nahi likha, bas default chai ka blueprint badal kar 'MasalaChai' kar diya
    chai_cls = MasalaChai


# Yahan humne normal dukan ka object banaya. 
# Iske andar 'BaseChai' ka object banega.
shop = ChaiShop()

# Yahan humne fancy dukan ka object banaya. 
# Iske andar 'MasalaChai' ka object banega.
fancy = FancyChaiShop()

# Normal dukan ne chai serve ki (Output: Serving Regular chai in the shop \n Preparing Regular chai....)
shop.serve()

# Fancy dukan ne bhi chai serve ki. Dono ne same 'serve' method use kiya jo Parent ChaiShop mein tha.
fancy.serve()

# Yahan hum fancy dukan ke andar rakhi chai ('MasalaChai' object) ko direct command de rahe hain ki masale daalo.
# Yeh chal jayega kyunki 'MasalaChai' ke paas 'add_spices' method hai.
# Agar hum 'shop.chai.add_spices()' likhte toh Error aata, kyunki normal shop ke paas 'BaseChai' hai jisme masale dalne ka method nahi hai!
fancy.chai.add_spices()