Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> # spilt() vs join() ==> string functions
>>> 
>>> str1 = "India is a great country"
>>> 
>>> str1
'India is a great country'
>>> 
>>> type(str1)
<class 'str'>
>>> 
>>> # The split function will devide the string based on given delimeter
>>> # and retunrs a list of strings
>>> 
>>> str1.split("is")
['India ', ' a great country']
>>> 
>>> str1.split("a")
['Indi', ' is ', ' gre', 't country']
>>> str1.split() # deafult space is delimter
['India', 'is', 'a', 'great', 'country']
>>> 
>>> x = ['India', 'is', 'a', 'great', 'country']
>>> # *
>>> output = ""
>>> for word in x:
	output = output + "*"

>>> print(output)
*****
>>> for word in x:
	output = output + word + "*"

	
>>> print(output)
*****India*is*a*great*country*
>>> 
>>> 
>>> 
>>> x
['India', 'is', 'a', 'great', 'country']

>>> 
>>> dle = "*"
>>> 
>>> dle.join(x)
'India*is*a*great*country'
>>> 
>>> 
>>> ip = '10.221.49.88'
>>> 
>>> 
>>> ip
'10.221.49.88'
>>> 
>>> 
>>> x = ip.split(".")
>>> 
>>> 
>>> x
['10', '221', '49', '88']
>>> 
>>> 
>>> ".".join(x)
'10.221.49.88'
>>> "Vishnu".join(x)
'10Vishnu221Vishnu49Vishnu88'
>>> 
>>> 
