"""
def myupper(str1):  # bangalore
    output = ""
    for ch in str1:
        if ord(ch) >= 97 and ord(ch) <= 122:
             ch = chr(ord(ch) - 32)
             output = output+ch
        else:
            output = output+ch
        
    return output
"""
def myupper(str1):  # bangalore
    output = ""
    for ch in str1:
        if ord(ch) >= 97 and ord(ch) <= 122:
             ch = chr(ord(ch) - 32)
        output = output+ch
        
    return output

x = input("Enter a 1st value: ")

resp = myupper(x)


print("Response : ", resp)
