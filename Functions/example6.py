# join() ['a', 'n', 'e', 'm'] ==> a-b-c-d

"""
def myjoin(x_list, del_str):
    output = ""
    for item in  x_list: 
        output = output+item+del_str
    print(output)
        
x = ['a', 'n', 'e', 'm']

myjoin(x, '-')
"""

def myjoin(x_list, del_str):
    output = ""
    for i in range(0, len(x_list)-1): 
        output = output+x_list[i]+del_str
    #print(output)
    output = output+x_list[-1]
    return output
        
x = ['a', 'n', 'e', 'm']

myjoin(x, '-')
