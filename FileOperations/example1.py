# WAP read the data from given input.txt file


"""
open a file

writing data inside a file

closing the file




open a file

read the content from the file

cloase the file


open a file
update the data file

close the file



open ==> read/write/append  ==> close

"""
# How to open a file

#<returns_file_object> open(filepath, mode)
# filepath ==> string type
# mode ==> string type
"""
To open a file we have to use open() function

The open() function will take two parameters path and mode of the operations

r --> read mode
w --> write mode
a --> appending

The open() function will returns the file object ==>

"""
# How to read

"""
To read the from the file we have function called read()
the read() function reads entire data from the file as a STRING type
"""


f = open("input.txt", 'r')  # f is a file object
data = f.read()
#print(type(data))
f.close()
print(data)















