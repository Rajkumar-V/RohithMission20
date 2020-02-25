# Variable number of argumnets to the functions

"""
Design a add function it should take N number argumnets and it shoud
compute some

Using *arg parameter we can pass variable number of argumnets to the function
"""

def add(*args):
    s = 0
    for i in args:
        s = s+i
    return s


print(add(10))


print(add((10, 20)))

print(add(10, 20, 30))

print(add(10, 10, 20, 30, 40))


def add(t_tuple):
    s = 0
    for i in args:
        s = s+i
    return s
