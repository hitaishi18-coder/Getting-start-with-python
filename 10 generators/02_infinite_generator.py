def infinite_cake():
    count = 1 
    while True:
        yield f"refill #{count}"
        count+=1
print(infinite_cake())
refill_1 = infinite_cake()
refill_2 = infinite_cake()

for _ in range(5):
    print(next(refill_1))

for _ in range(10):
    print(next(refill_2))