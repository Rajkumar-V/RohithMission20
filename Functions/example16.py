#   Recursive functions
#  Calling  a same function itself


#  WAP find factorial of a given number

# 5! =5 * 4* 3* 2*1

"""
def get_fact(n):
    fact = 1
    if n <= 0:
        return 1

    else:
        for i in range(n, 0, -1):
           fact = fact * i
    return fact

print(get_fact(5))

"""
# 5! = 5*4!
# 4! = 4* 3!
# 3! = 3*2!
# 2! = 2*1!
# 1! = 1

import sys

def get_fact_rec(n):
    if n <= 0:
        return 1
    else:
        return n *get_fact_rec(n-1)


sys.setrecursionlimit(5000)

print(get_fact_rec(1090))






