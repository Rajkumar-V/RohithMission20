# break & continue ==> inside loops

# break ==> breaks the loop with certain condition

# continue  ==> will skip the iterations with with certain condition


# WAP print all the number from the given list till the number 7 encounters
"""
x = [10, 2, 6, 7, 19, 76]


for e in x:
    if e == 7:
        break
    print(e)
"""

# WAP print all the numbers from the gievn list except the numbers which are
# divisible 4

x = range(2, 20) # 2, 3, 4, 5, 6, 
    
for i in x:
    if i % 4 == 0:
        continue
    print(i)

