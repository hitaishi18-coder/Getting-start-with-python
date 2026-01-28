# -------- Example 1: Set comprehension to get unique chai types --------

favourite_chais = [
    "masala chai", "green tea", "masala chai",
    "lemon tea", "green tea", "elaichi chai"
]

# Set comprehension removes duplicate chai names
unique_chai = {chai for chai in favourite_chais}

print(unique_chai)
print("------------------------")


# -------- Example 2: Nested set comprehension to get unique spices --------

recipe = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}

# Loop through each recipe's ingredient list,
# then through each spice to collect unique spices
unique_spices = {spice for ingredients in recipe.values() for spice in ingredients}

print(unique_spices)
print("------------------------")
