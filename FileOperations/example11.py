# Writing data inside a file
"""
If we are opening a file in write mode

when the file is not exist it will create a new file
if it is exit it will overide the content 
"""
# To write the data inside a file we have a function
# defined i.e write(<data_as_a_string_format>) 

f = open('output.txt', 'w')

f.write("Hello Welcome to python world")
f.close()



