class Chai:
    origin = "india"

print(Chai.origin)

Chai.is_hot = True

masala = Chai()
print(f"masala {masala.origin}")
print(f"masala {masala.is_hot}")
masala.is_hot = False

print(f"masala", Chai.is_hot)
print(f"masala {masala.is_hot}")

masala.flavor = "masala"
print(masala.flavor)