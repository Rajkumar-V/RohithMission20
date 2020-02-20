# WAP add two numbers & three numbers

"""
anything in multiple forms --> Polymorphsim

Function Overloading :  NO FUNCTION OVERLOADING SUPPORT
    Same function name with different jobs 

Function Overiding :

if you define different functions with same name
the latest defined function will be overrides with previous defined function
"""


def add(x, y):
    return x+y


print("Adding two numbers: ", add(10, 20)) # 30


def add(x, y, z):
    return x+y+z

print("Adding three numbers: ", add(100, 200, 300)) # 600


print("Adding two numbers: ", add(1000, 2000)) # 3000
