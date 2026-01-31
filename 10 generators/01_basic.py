def serve_cake():
    yield "cake1 : chocolate cake"
    yield "cake2 : cheese cake"
    yield "cake3 : truffle choco cake"

cake = serve_cake()
# for c in cake:
#     print(cake)

def cake_list():
    return [ "cheese cake", "choco cake","truffle cake"]
print(cake_list())


# generator function 
def cake_generator():
    yield "choco cake"
    yield "cheese cake"
    yield "truffle cake"
cake = cake_generator()
print(next(cake))
print(next(cake))
print(next(cake))