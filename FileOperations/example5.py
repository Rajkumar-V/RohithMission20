# WAP count total number of words from the file


f = open('input.txt', 'r')

data = f.read() # returns entire data from the file as a STRING

f.close()


words = data.split()

print(len(words))


# add to list
