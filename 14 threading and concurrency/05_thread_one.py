import threading
import time 

def chai_making():
    print(f"boil chai")
    time.sleep(2)
    print("chai is boiled..")

def toast_make():
    print(f"toast making")
    time.sleep(3)
    print(f"toast is maked")

start = time.time()

t1 = threading.Thread(target=chai_making)
t2 = threading.Thread(target=toast_make)


t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds")