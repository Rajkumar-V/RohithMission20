# WAP read the data from the file and display all the words which are starts witj
# i or I


f = open('input.txt', 'r')

data = f.read()

f.close()


words = data.split()
#print(words)

for word in words:
    #print(word, type(word))
    if word[0] == 'i' or word[0] == 'I':
        print(word)

