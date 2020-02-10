

# Read the data from the file1.txt and file2.txt

# and display all the words from the file1 which are starts with h or m

# and display all the words from the file2 which are starts with c or s

path = ".\dependecies\\file1.txt"  # Reletive path for file1

f = open(path, 'r')

text1 = f.read()
f.close()

words =  text1.split()

words_from_file1= []
for word in words:
    #print(word)
    if word[0] == "h" or word[0] == 'm':
        words_from_file1.append(word)
print("Data from file1")
print(words_from_file1)

print("="*100)

path2 = ".\dependecies\\file2.txt"

f = open(path, 'r')
text2 = f.read()
f.close()


words =  text2.split()

words_from_file2 = []
for word in words:
    if word[0] == 'c' or word[0] == 's':
        words_from_file2.append(word)
print("Data from file2")
print(words_from_file2)




