Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> s1 = "BANGALORE"
>>> 
>>> s1
'BANGALORE'
>>> type(s1)
<class 'str'>
>>> 
>>> c = 'M'
>>> c
'M'
>>> type(c)
<class 'str'>
>>> s1 = BANGALORE
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s1 = BANGALORE
NameError: name 'BANGALORE' is not defined
>>> 
>>> s1
'BANGALORE'
>>> # 1st char
>>> s1[0]
'B'
>>> # 2nd  Char
>>> s1[1]
'A'
>>> 
>>> # 3rd Char
>>> s1[2]
'N'

>>> # Last char
>>> s1[8]
'E'
>>> s1[9]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1[9]
IndexError: string index out of range
>>> 
>>> 
>>> # len(object) # returns size or length of an object
>>> 
>>> len(s1)
9
>>> size = len(s1)
>>> 
>>> size
9
>>> s1[size-1]
'E'
>>> s1[len(s1)-1]
'E'
>>> 
>>> # Using indexing we can access individual element
>>> 
>>> 
>>> # Concatenation : Cobining two strings
>>> 
>>> s1
'BANGALORE'
>>> s2 = " City"
>>> len(s2)
5
>>> s1+s2
'BANGALORE City'
>>> 
>>> 
>>> s3 = s1 + s2
>>> 
>>> s3
'BANGALORE City'
>>> 
>>> 
>>> # Slicing
>>> s3[3:8]
'GALOR'
>>> s3[4:]
'ALORE City'
>>> s3[:]
'BANGALORE City'
>>> 
>>> s3[:8]
'BANGALOR'
>>> 
>>> # Indexing, Concatenation , Slicing , SIZE ==> len()
>>> 
>>> s1
'BANGALORE'
>>> 
>>> # Repetition
>>> 
>>> s1*2
'BANGALOREBANGALORE'
>>> s1*4
'BANGALOREBANGALOREBANGALOREBANGALORE'
>>> 
>>> 
>>> 
