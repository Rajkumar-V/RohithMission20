def read_file(filepath):
    try:
        f = open(filepath, 'r')
        d = f.read()
        f.close()
        return d
    except FileNotFoundError:
        print("Please check file path: {}".format(filepath))
    except IOError:
        print("Unable to raed the data from the file:{}".format(filepath))
    except Exception as e:
        print("Unknow read file error: " + str(e))

def write_file(filepat, content):
    f = open(filepath, 'w')
    f.write(content)
    f.close()


    


read_file("asasd")
