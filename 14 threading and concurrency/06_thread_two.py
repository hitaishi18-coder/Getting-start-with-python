import threading
import time

def prepare_chai(type, wait_time):
    print(f"{type} chai is brewing ..")
    time.sleep(wait_time)
    print(f"{type} chai is brewed...")


t1 = threading.Thread(target=prepare_chai, args=("masala",2))
t2 = threading.Thread(target=prepare_chai, args=("ginger",5))


t1.start()
t2.start()
t1.join()
t2.join()