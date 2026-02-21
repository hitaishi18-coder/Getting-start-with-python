import threading
import time

def chai(type, wait_time):
    print(f"{type}  start chai...")
    time.sleep(wait_time)
    print(f"{type} end chai...")

t1 = threading.Thread(target=chai,args=("masala",2))
t2 = threading.Thread(target=chai,args=("elaichi",4))

t1.start()
t2.start()

t1.join()
t2.join()