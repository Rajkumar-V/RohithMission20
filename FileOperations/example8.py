# WAP read all the lines from the file which are starting with "If"

f = open('zen_of_python.txt', 'r')

lines = f.readlines()
f.close()

for line in lines:
    #print(line)
    if line.startswith('If'):
        print(line)
        
