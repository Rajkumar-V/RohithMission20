Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> # membership operators
>>> 
>>> # in and not in
>>> 
>>> x = [10, 20, 30, 40]
>>> x
[10, 20, 30, 40]

>>> 10 in x
True
>>> 50 in x
False
>>> 50 not in x
True
>>> x = "ABCDE"
>>> 
>>> "A" in x
True
>>> "AB" in x
True
>>> "ABD" in x
False
>>> "ABD" not in x
True
>>> d = {"A": 65, "B": 66}
>>> d
{'A': 65, 'B': 66}
>>> "A" in d
True
>>> "E" in d
False
>>> 65 in d
False
>>> 65 in d.values()
True
>>> 
>>> 
