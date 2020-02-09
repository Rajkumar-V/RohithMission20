Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Defining a tuple
>>> 
>>> x = (10, 20, 30, 40)
>>> x
(10, 20, 30, 40)
>>> 
>>> type(x)
<class 'tuple'>
>>> 
>>> # Indexing
>>> x
(10, 20, 30, 40)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> x[0]
10
>>> x[1]
20
>>> y = [50, 60, 70]
>>> y
[50, 60, 70]
>>> y = (50, 60, 70)
>>> 
>>> x+y
(10, 20, 30, 40, 50, 60, 70)
>>> z = x+y
>>> z
(10, 20, 30, 40, 50, 60, 70)
>>> z[2:5]
(30, 40, 50)
>>> y*3
(50, 60, 70, 50, 60, 70, 50, 60, 70)
>>> len(x)
4
>>> len(y)
3
>>> 
>>> 
>>> x = [10, 20, 67.8, "xyz", "abc", [10, 20], (10, 20)]
>>> 
>>> 
>>> x
[10, 20, 67.8, 'xyz', 'abc', [10, 20], (10, 20)]
>>> 
>>> 
>>> 
>>> y = (10, 20, 67.8, "xyz", "abc", [10, 20], (10, 20))
>>> 
>>> y
(10, 20, 67.8, 'xyz', 'abc', [10, 20], (10, 20))
>>> x
[10, 20, 67.8, 'xyz', 'abc', [10, 20], (10, 20)]

>>> 
>>> 
>>> x[0] = 1000
>>> 
>>> x
[1000, 20, 67.8, 'xyz', 'abc', [10, 20], (10, 20)]
>>> 
>>> 
>>> y
(10, 20, 67.8, 'xyz', 'abc', [10, 20], (10, 20))
>>> 
>>> 
>>> y[0] = 1000
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    y[0] = 1000
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> str1 = "BANAGLORE"
>>> 
>>> str1
'BANAGLORE'
>>> str1[0] = "M"
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    str1[0] = "M"
TypeError: 'str' object does not support item assignment

>>> 
>>> 
>>> # Mutable vs Immutable
>>> 
>>> # Mutable : List
>>> # Immutable : Tuple, Strings
>>> 
>>> # What about the numbers?
>>> 
>>> a = 10
>>> a
10
>>> id(a)
255641664
>>> 
>>> a = 30
>>> 
>>> a
30
>>> id(a)
255641984
>>> 
>>> c = 10
>>> 
>>> id(c)
255641664
>>> 
>>> type(c)
<class 'int'>
>>> 
