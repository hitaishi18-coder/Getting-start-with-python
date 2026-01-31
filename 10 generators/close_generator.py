def local_chai():
    yield "milk tea"
    yield "green tea"

def imported_chai():
    yield "matcha"
    yield "oolong"

def full_chai():
    yield from local_chai()
    yield from imported_chai()

for chai in full_chai():
    print(chai)

#...........

def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed, no more chai ..")

stall = chai_stall()
print(next(stall))
stall.close()
