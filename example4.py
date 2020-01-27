Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # WAP convert given string s1 = "BANGALORE" to "MANGALORE"
>>> s1 = "BANGALORE"
>>> s1
'BANGALORE'
>>> s1[0]
'B'
>>> s1[0] = 'M'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s1[0] = 'M'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> # Strings are constant or read-only object in python
>>> s1[1:]
'ANGALORE'
>>> "M" + str1[1:]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    "M" + str1[1:]
NameError: name 'str1' is not defined
>>> "M" + s1[1:]
'MANGALORE'
>>> 
