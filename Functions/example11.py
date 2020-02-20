def read_file(filepath):
    f = open(filepath, 'r')
    d = f.read()
    f.close()
    return d

def write_file(filepath, content, mode='w'):
    print("MODE: ", mode)
    f = open(filepath, mode)
    f.write(content)
    f.close()
"""
def append_file(filepath, content):
    f = open(filepath, 'a')
    f.write(content)
    f.close()
"""

#write_file("new_output.txt", "CONTENT")

#write_file("new_output.txt", "ANOTHELINE")

lines = ["Line1", "Line2", "Line3"]
for line in lines:
    write_file("lines.txt", line, 'a')
