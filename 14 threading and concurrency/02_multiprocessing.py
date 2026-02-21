from multiprocessing import Process
import time

def brew_chai(name):
    print(f"start of the {name} chai brewing")
    time.sleep(3)
    print(f"end of the {name} chai brewing")

if __name__ == "__main__":
    chai_maker = [
        Process(target=brew_chai, args=(f"chai maker {i+1}" , ))
        for i in range(3)   
    ]

    #start process 

    for p in chai_maker:
        p.start()
    
    # wait for all to finish
    for p in chai_maker:
        p.join()

    print("all chai served...")