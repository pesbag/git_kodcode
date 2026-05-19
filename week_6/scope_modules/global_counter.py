count = 0
def bumb():
    global count
    count+=1
def value():
    return count

bumb(),bumb(),bumb()
print(value())