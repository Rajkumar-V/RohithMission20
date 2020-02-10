# WAP read all the lines from the file which are starting with "A" and "I
import time

f = open('zen_of_python.txt', 'r')
text = f.read()    # readlines()
f.close()

#print(text)


lines = text.split("\n") # \n is new line character
#print(lines)

for line in lines:
    if len(line) > 0:
        if line[0] == 'A' or line[0] == 'I':
             print(line)

