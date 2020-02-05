# WAP find all each occurance of a vowel count from the given string


d = {} # Place hoder to store the output

str1 = "hyderabad"

vowels = "aeiou"

for ch in str1:
    if ch in vowels:
        if ch not in d:
             d[ch] = 1 # d['e'] = 1 ==> {'e':1}
        else:
            d[ch] = d[ch] +1
print(d)






#d= {'a':2, 'e':1}
