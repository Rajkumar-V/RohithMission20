"""
Exception Handling
Exceptios are runtime errors

try: Which ever the exceptional causing statemnets we need put inside try-block
except: Once exception arises what action user has to take we need put inside
except block
raise*
finally*
else*
"""

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    try:
        return x//str(y)
    except ZeroDivisionError:
        print("Please enter second value as non zero value")
    except Exception as e:
        print("Unknown error: " + str(e))
 
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

op = input("Enter your choise: (1- add, 2-sub 3-mul 4-div):")

if op == '1':
    print(add(a, b))
elif op == '2':
    print(sub(a, b))
elif op == '3':
    print(mul(a, b))
elif op =='4':
    print(div(a, b))
else:
    print("Invalid option")
