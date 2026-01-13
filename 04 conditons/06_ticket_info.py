# you are building a ticket info system for a railway app

# based on seat type ..  show its features 

# task : 
#      input : "sleeper" , "AC" , "general","luxury"
#      match using match-case 
#      unknown - show: "invalid seat type"


seat_type = input("enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type :
    case "sleeper":
        print("sleeper - no AC , beds available")
    case "ac":
        print("ac - air conditioned and comfy")
    case "general":
        print("general - cheapest option , no reservation")        
    case "luxury":
        print("luxury- premium seats with meals")
    case _ :
        print("invalid seat type")