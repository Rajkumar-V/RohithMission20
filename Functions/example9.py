# Returning a multiple values from the functions

# Find avg and sum for given x



def get_sum_avg_of_list(x):
    s = 0
    for i in x:
        s = s+i
    #avg = s//len(x)
    #return s, avg
    return s, s//len(x)


input_x = range(10)


"""
sum_, avg_ = get_sum_avg_of_list(input_x)
print("Sum ", sum_)
print("Avg ", avg_)
"""


y  = get_sum_avg_of_list(input_x)

print(type(y))

print("Sum : ", y[0])
print("Avg: ", y[1])
