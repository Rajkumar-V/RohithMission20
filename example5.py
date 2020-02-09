Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> 
>>> len(x)
4
>>> 
>>> y = (10, 20, 30, 40)
>>> y
(10, 20, 30, 40)

>>> type(y)
<class 'tuple'>
>>> 
>>> len(y)
4
>>> # Indexing
>>> y[0]
10
>>> y[1]
20
>>> y[len(y) -1]
40
>>> y
(10, 20, 30, 40)
>>> z = (70, 80, 90)
>>> z
(70, 80, 90)
>>> len(z)
3
>>> type(z)
<class 'tuple'>
>>> y+z
(10, 20, 30, 40, 70, 80, 90)
>>> 
>>> 
>>> w = y+z
>>> 
>>> w
(10, 20, 30, 40, 70, 80, 90)

>>> 
>>> type(w)
<class 'tuple'>
>>> len(w)
7
>>> 
>>> w[3:7]
(40, 70, 80, 90)
>>> 
>>> 
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> x
[10, 20, 30, 40]
>>> 
>>> 
>>> 
>>> y
(10, 20, 30, 40)
>>> y*4
(10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)
>>> 
>>> 
>>> 
>>> x = [10, 20, 50.8, "xyz", [10, 20, 30]]
>>> 
>>> x
[10, 20, 50.8, 'xyz', [10, 20, 30]]
>>> 
>>> len(x)
5
>>> 
>>> x = (10, 20, 50.8, "xyz", [10, 20, 30])
>>> 
>>> x
(10, 20, 50.8, 'xyz', [10, 20, 30])
>>> 
>>> type(x)
<class 'tuple'>
>>> 
>>> x = [10, 20, 30]
>>> 
>>> x
[10, 20, 30]

>>> x[0] = 1000
>>> 
>>> x
[1000, 20, 30]

>>> 
>>> y = (10, 20, 30)
>>> y
(10, 20, 30)
>>> 
>>> y[0] = 1000
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    y[0] = 1000
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # Define all the vowels
>>> 
>>> 
>>> x = ['a', 'e', 'i', 'o', 'u']
>>> 
>>> x
['a', 'e', 'i', 'o', 'u']

>>> vowels = ['a', 'e', 'i', 'o', 'u']
>>> 
>>> 
>>> vowels
['a', 'e', 'i', 'o', 'u']
>>> 
>>> 
>>> vowels = ('a', 'e', 'i', 'o', 'u')
>>> 
>>> vowels
('a', 'e', 'i', 'o', 'u')

>>> vowels = "aeiou"
>>> 
>>> 
>>> 
