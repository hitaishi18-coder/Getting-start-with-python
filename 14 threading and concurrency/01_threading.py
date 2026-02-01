import threading
import time 

def take_order():
    for i in range(1,4):
        print(f"taking order in range {i}")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"chai is brewing {i}")
        time.sleep(3)

# create threads 
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

# start 
order_thread.start()
brew_thread.start()

# wait for finish 
order_thread.join()
brew_thread.join()

print("all orders are taken and chai is brewed !! ")