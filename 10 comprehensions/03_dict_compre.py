# Dictionary containing tea prices in INR
tea_prices_inr = {
    "masala chai": 40,
    "green chai": 50,
    "lemon chai": 200
}

# Dictionary comprehension to convert prices from INR to USD
# Assuming 1 USD = 80 INR
tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}

# Print original INR prices
print("Prices in INR:", tea_prices_inr)

# Print converted USD prices
print("Prices in USD:", tea_prices_usd)
