# WAP upadate each key-value from the dict with respective calue + 100

d = {"A": 65, "B": 66, "C": 67, "D": 68}



for k in d:
    #print(k)
    d[k] = 100+d[k]

print(d)
