# WAP reverse a string


"""
def str_reverse(str1_input):
    output = ""
    for i in str1_input:
        print(i)
        output= i+output
        print(output)
    return output
"""
"""
def str_reverse(str1_input):
    output = ""
    for i in range(len(str1_input)-1, -1, -1):
        print(str1_input[i])
        output = output+str1_input[i]
    print(output)

"""

def str_reverse(str1_input):
    output = ""
    for i in range(1, len(str1_input)+1):
        #print(-i)
        #print(str1_input[-i])
        output = output+ str1_input[-i]
    return output

str1 = "hyderabad"
print(str_reverse(str1))
