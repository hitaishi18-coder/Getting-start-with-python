# 'TeaLeaf' class jisme hum data ko protect karna seekhenge (Encapsulation).
class TeaLeaf:
    
    # Constructor jo patti ki initial age set karta hai.
    def __init__(self, age):
        # Dhyan dein: 'age' ke aage underscore '_' laga hai. 
        # Yeh Python mein ek ishara (warning) hai ki yeh variable "Protected/Private" hai.
        # Iska matlab hai: "Bhai, is variable ko class ke bahar se direct use ya change mat karna!"
        self._age = age

    # @property ek magic tag hai jo is method (function) ko ek normal variable jaisa bana deta hai.
    # Ise 'Getter' kehte hain. Iska kaam hai data ko bahar bhejna.
    @property
    def age(self):
        # Jab koi bahar se 'leaf.age' mangega, toh background mein yeh function chalega.
        # Yeh actual age (jo '_age' mein hai) usme 2 jod kar bahar bhej dega.
        # Fayda: Bahar wale ko pata hi nahi chala ki andar kya calculation hui aur asli age kya hai!
        return self._age + 2
    
    # @age.setter humara "Security Guard" (Bouncer) hai.
    # Ise 'Setter' kehte hain. Iska kaam hai naye data ko check karke hi andar aane dena.
    @age.setter
    def age(self, age):
        # Agar koi bahar se 'leaf.age = 4' likhta hai, toh wo yahan check hone aayega.
        # Condition: Kya nayi age 1 se 5 ke beech hai?
        if 1 <= age <= 5:
            # Agar haan, toh safely actual '_age' ko update kar do.
            self._age = age
        else:
            # Agar nahi (jaise kisine 6 ya 100 daal diya), toh turant Error (ValueError) throw kar do!
            # Isse humara object galat data se bach jayega.
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        

# Humne ek naya object banaya aur uski actual age 2 set kar di.
leaf = TeaLeaf(2)

# Yahan hum variable ko read kar rahe hain, toh chupke se @property (Getter) chalega.
# Actual age 2 thi, toh (2 + 2) return hoga.
# Output: 4
print(leaf.age)


# YAHAN ASLI TEST HAI!
# Yahan hum variable ko update kar rahe hain, toh @age.setter (Guard) chalega.
# Humne age 6 daalne ki koshish ki. Guard check karega (1 <= 6 <= 5) jo ki False hai.
# Result: Code yahi par CRASH ho jayega aur ValueError aayega!
# (Yeh ek achhi baat hai, humari security perfectly kaam kar rahi hai).
leaf.age = 6

# Kyunki code upar wali line mein hi crash ho chuka hai (Error ki wajah se), 
# yeh print line kabhi chalegi hi nahi.
print(leaf.age)