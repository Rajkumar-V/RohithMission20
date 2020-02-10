# WAP count total number of words from the file
import time

f = open('input2.txt', 'r')

lines = f.readlines() # returns entire data from the file as a LIST

f.close()


print(lines)


for line in lines:
    # Wait time
    time.sleep(2)
    print(line)
