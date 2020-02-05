# WAP upadate each key-value from the dict with respective hexdecimal value 

d = {"A": 65, "B": 66, "C": 67, "D": 68}


for k in d:
    d[k] = hex(d[k])
print(d)
