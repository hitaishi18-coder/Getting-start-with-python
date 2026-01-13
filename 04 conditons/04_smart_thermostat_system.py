# you are building a small thermostat alert system:

# if the device_status is "active"
#    and temperature > 35 --> warm : "high temperature alert!"
#    else : "temperature normal"
# if device is off --> "device is offline"


device_status = "active"
temperature =  35

if device_status == "active":
    if temperature > 35 :
        print("high temperature alert!")
    else:
        print("temperature is normal ")    
else:
    print("device is offline !")