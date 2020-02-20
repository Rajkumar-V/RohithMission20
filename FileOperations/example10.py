

def read_file(filepath):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data


path = 'input.txt'


text = read_file(path)
print(text)


