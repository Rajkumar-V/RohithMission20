#  WAP add two numbers and multiply result with 100


# The variable which are defined inside a function are the local variable to that function

# We are not allowed to access local variable outside of the function definition
def add(x, y):
    c = x+y
    #print(c)
    return c


a = 10
b = 20

s = add(a, b)

print("Return value of function: ", s)
print(s*100)

"""
- To access the values computes inside a function to the outside of teh functiin
definitiom we have to retirn the value by using return statement

returning value from the function & collecting the values from the function definition is an optional


If you are not retrning anything from the function by default it is None
"""

#print(c*100) # Error


