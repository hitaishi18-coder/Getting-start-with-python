import threading 
import time 

def boil_milk():
    print(f"boil milk")
    time.sleep(2)
    print(f"milk boiled")

def toast_bun():
    print(f"toast is making ")
    time.sleep(3)
    print(f"toast maked")

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds")