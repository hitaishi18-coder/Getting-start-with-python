import threading
import time

def monitoring_chai_temperature():
    while True:
        print(f"monitoring tea temperatue .. ")
        time.sleep(6)

t = threading.Thread(target=monitoring_chai_temperature, daemon=True)
t.start()

print("main program done ..")