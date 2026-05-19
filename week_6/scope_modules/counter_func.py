def make_counter():
    n=0
    def add_1():
        nonlocal n
        n+=1
        return n
    return add_1

c=make_counter()
print(c(),c(),c())