# A tea stall offers different prices for different cup sizes 
# write a program that calculates the price based on size 

# task : 
#      input "small" , "medium" , "large"
#      small --> rs 10 , medium --> rs 15 , large --> rs 20
#      if invalid : show "unknown cup size" 


cup = input("choose your cup size (small/ medium/ large) ").lower()

if cup == "small" :
    print("price is RS 10/-")
elif cup == "medium":
    print("price is Rs 15/-")    
elif cup == "large":
    print("price is Rs 20/-")    
else :
    print("unknown cup size ! ")    