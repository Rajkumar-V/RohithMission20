Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> x = []
>>> type(x)
<class 'list'>
>>> 
>>> x = [10, 20, 30, 40, 50]
>>> x
[10, 20, 30, 40, 50]
>>> type(x)
<class 'list'>
>>> len(x)
5
>>> 
>>> 
>>> x[0] # 1st element
10
>>> x[1] # 2nd element
20
>>> x[len(x)-1]
50
>>> x
[10, 20, 30, 40, 50]
>>> y = [40, 90, 80]
>>> y
[40, 90, 80]
>>> x+y  #  [10, 20, 30, 40, 50, 40, 90, 80]
[10, 20, 30, 40, 50, 40, 90, 80]
>>> 
>>> 
>>> z = x+y
>>> z
[10, 20, 30, 40, 50, 40, 90, 80]
>>> 
>>> 
>>> # Slicing
>>> 
>>> z[1:5]
[20, 30, 40, 50]
>>> 
>>> z[:7]
[10, 20, 30, 40, 50, 40, 90]
>>> z[3:]
[40, 50, 40, 90, 80]
>>> 
>>> y*3
[40, 90, 80, 40, 90, 80, 40, 90, 80]
>>> 
>>> 
>>> # Defining ==[]
>>> # Seqntial object
>>> 
>>> 
>>> 
>>> # Operations : indexing, slicing, concatenation , Repet, SIZE
>>> 
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> # Using indexing not accessing the indvidual elements, but we can also change the elements
>>> x
[10, 20, 30, 40, 50]

>>> 
>>> 
>>> x[0]
10
>>> x[0] = 1000
>>> x
[1000, 20, 30, 40, 50]
>>> 
>>> x[0]
1000

>>> x[2] = "VISHNU"
>>> 
>>> x
[1000, 20, 'VISHNU', 40, 50]
>>> 
>>> 
>>> 
