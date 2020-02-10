

"""

open ==> read/writing/append ==> close()


fileobject open(<filepath>, mode)

r - read
w - write
a - append
"""

f = open('input.txt', 'r')

data = f.read() # returns entire data from the file as a STRING

f.close()


print(data)
