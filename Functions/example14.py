# Execute a program through command line & Command line args

import sys


def add(x, y):
    return x+y




if __name__ == "__main__":

    args = sys.argv[1:]
    if len(args) != 2:
        print("USAGE: python <program.py> arg1 arg2")
    else:
        print(add(int(args[0]), int(args[1])))





#print(add(10, 20))
"""

x = int(input("Enter a 1st value: "))

y = int(input("Enter a second value: "))

resp= add(x, y)
print(resp)
"""
