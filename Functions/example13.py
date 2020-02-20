"""

def add2(x, y):
    return x+y

def add3(x, y, z):
    return x+y+z
"""

# Default argumets

def add(x, y, z=0):
    return x+y+z


print("Adding 3 numbers: ", add(10, 20, 30))
print("Adding 2 numbers: ", add(10, 20))
