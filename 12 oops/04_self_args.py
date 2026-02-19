# 'Chaicup' naam ki ek class banayi
class Chaicup:
    # Yeh Class Variables (sabke default data) hain
    size = 150  # ml
    quantity = "normal"

    # Yeh ek function hai jo class ke andar hai, isliye isko "Method" kehte hain.
    # 'self' ka aasan matlab hai: "Yeh wala object" (jisne is method ko call kiya hai).
    def describe(self):
        # self.size aur self.quantity ka matlab hai ki us specific cup ka data laao
        return f"A {self.size}ml {self.quantity} chai cup"

# 'cup' naam ka ek naya object banaya
cup = Chaicup()


# TARIKA 1: Object ka use karke method call karna (Short/Normal way)
# Yahan humne bracket () khali chhoda hai. 
# Python background mein chupke se 'cup' ko utha kar 'describe' ke andar daal deta hai, jo 'self' ban jata hai.
# Output: A 150ml normal chai cup
print(cup.describe())

# TARIKA 2: Class ka use karke method call karna (Long/Actual way)
# Yahan hum seedha Class ('Chaicup') se method bula rahe hain. 
# Class ko nahi pata ki kis cup ki baat ho rahi hai, isliye humein khud 'cup' pass karna padta hai.
# Yahi 'cup' method mein jakar 'self' ki jagah le leta hai. Dono tariko ka output same aayega!
# Output: A 150ml normal chai cup
print(Chaicup.describe(cup))


# Ek aur naya object banaya 'cup_two' naam se
cup_two = Chaicup()

# Is 'cup_two' ko apna personal (instance) size de diya
cup_two.size = "medium "

# Ab jab hum 'describe' call karte hain aur 'cup_two' pass karte hain, toh 'self' = 'cup_two' ho jata hai.
# Isliye output mein Class wala 150ml nahi, balki cup_two ka apna "medium" size aayega.
# Output: A medium ml normal chai cup
print(Chaicup.describe(cup_two))