# WAP find all each occurance of a vowel count from the given string

a = 0
e = 0
i = 0
o = 0
u = 0
str1 = "hyderabad-banaglore-india"

for ch in str1:
    if ch == 'a':
        a = a+1
    elif ch == 'e':
        e = e+1
    elif ch == 'o':
        o = o+1
    elif ch == 'i':
        i = i +1
    elif ch == 'u':
        u = u+1
print("a count: ", a)        
print("e count: ", e)
print("i count: ", i)
print("o count: ", o)
print("u count: ", u) 
