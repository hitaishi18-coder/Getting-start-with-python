# 'ChaiUtils' (Chai Utilities) naam ki ek class banayi.
# Ise hum ek 'Toolbox' ki tarah use karenge jisme humare saare helper tools (functions) rakhe honge.
# Is class ka hum koi object nahi banayenge.
class ChaiUtils:
    
    # @staticmethod ek special tag (decorator) hai.
    # Yeh Python ko batata hai: "Bhai, is function ko kaam karne ke liye kisi object ('self') ki zaroorat nahi hai. 
    # Yeh ek normal independent function hai, bas isko main class ke andar rakh raha hoon taaki code saaf rahe."
    @staticmethod
    def clean_ingredients(text):
        # Yahan do cheezein ho rahi hain:
        # 1. text.split(","): Yeh comma ke base par string ke tukde kar dega.
        # 2. item.strip(): Yeh har tukde ke aage aur peeche ke extra spaces (khali jagah) ko hata dega.
        # Aur final result ek List mein daal kar return kar dega.
        return [item.strip() for item in text.split(",")]
    

# Yeh humari ek raw string hai jisme bahut saare extra spaces aur commas hain
raw = " water , milk , ginger , honey "

# ASLI JAADOO YAHAN HAI:
# Dhyan se dekhiye, humne `utils = ChaiUtils()` karke koi naya object NAHI banaya!
# Kyunki yeh ek @staticmethod hai, hum seedha Class ke naam (ChaiUtils) ka use karke is function ko bula sakte hain.
cleaned = ChaiUtils.clean_ingredients(raw)

# Output print kar rahe hain
# Output: ['water', 'milk', 'ginger', 'honey'] (Sab ekdum saaf aur list format mein!)
print(cleaned)