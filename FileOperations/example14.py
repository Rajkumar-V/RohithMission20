def read_file(filepath):
    f = open(filepath, 'r')
    d = f.read()
    f.close()
    return d

def write_file(filepat, content):
    f = open(filepath, 'w')
    f.write(content)
    f.close()

def append_file(filepat, content):
    f = open(filepath, 'a')
    f.write(content)
    f.close()


    
