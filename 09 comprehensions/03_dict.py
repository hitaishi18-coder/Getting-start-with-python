cakes_price = {
    "chocolate cake": 50,
    "fruit cake" : 90,
    "dry cake" : 70
}

cakes_usd = {cake:price/80 for cake , price in cakes_price.items()}
print(cakes_usd)