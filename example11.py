Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Mutable vs Immutable
>>> """ 
Mutable means ==> We can change  ==> List
Immuatble means ==> We can not change  ==> Tuple, Strings

What about numbers?
"""
' \nMutable means ==> We can change  ==> List\nImmuatble means ==> We can not change  ==> Tuple, Strings\n\nWhat about numbers?\n'
>>> 
>>> 
>>> a = 10
>>> 
>>> 
>>> a
10
>>> type(a)
<class 'int'>
>>> id(a)
265930816
>>> 
>>> 
>>> a = 20
>>> 
>>> a
20
>>> type(a)
<class 'int'>
>>> id(a)
265930976
>>> 
>>> # Numbers are immutable objects in python
>>> c = 10
>>> id(c)
265930816
>>> 
