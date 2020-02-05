# without if statement can we write else? YES

"""

The else - block we can use not for condtional statements , we can also use
for iterative statements (for, while)
"""

# Once the successful execution the loop the else-block will execute
"""
x = [2, 4, 6, 8]

for i in x:
    print(i)
else:
    print("Success")
"""
"""
x = [2, 4, 6, 8]

for i in x:
    print(i)
else:
    print("Success")
"""
"""
x = [10, 2, 6, 7, 19, 76]


for e in x:
    if e == 17:
        break
    print(e)
else:
    print("After loop success")
"""


# WAP print all the numbers from the gievn list except the numbers which are
# divisible 4

x = range(2, 20) # 2, 3, 4, 5, 6, 
    
for i in x:
    if i % 4 == 0:
        continue
    print(i)
else:
    print("After loop success")







    
